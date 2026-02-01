import os
import sys
import io
import subprocess
import logging
import shutil
from mcp.server.fastmcp import FastMCP
from cookiecutter.main import cookiecutter

# 1. Fix encoding for Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 2. Create logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("Fast-MC-Kit")

server = FastMCP("Fast-MC-Kit")

# 3. Paths
MCP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(MCP_DIR)
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")
PLUGINS_DIR = os.path.join(BASE_DIR, "plugins")
TEMPLATE_DIR = os.path.join(BASE_DIR, "template")

def clean_path_input(raw_path: str) -> str:
    """Remove unused prefixes 'projects/' from AI input data."""
    p = raw_path.replace("\\", "/").strip("/")
    if p.startswith("projects/"):
        p = p[len("projects/"):]
    return p

def run_self_check():
    """Checkup when starting server."""
    print("\n" + "="*42)
    print("    FAST-MC-KIT MCP SERVER STARTUP    ")
    print("="*42)
    for name, path in [("Base", BASE_DIR), ("Projects", PROJECTS_DIR), ("Template", TEMPLATE_DIR)]:
        status = "[ OK ]" if os.path.exists(path) else "[MISSING]"
        print(f"[*] {name:<10}: {status} {path}")
    print("="*42 + "\n")

@server.tool()
def check_environment() -> str:
    """Checkup libs like Java, Maven and Python in the system."""
    logger.info("Checkup environment...")
    results = []
    for tool in ["java", "mvn", "python"]:
        path = shutil.which(tool)
        results.append(f"{'✔' if path else '✘'} {tool}: {'FOUND' if path else 'NOT FOUND'}")
    return "\n".join(results)

@server.tool()
def create_new_plugin(
    plugin_name: str, author: str, main_class: str, 
    description: str = "AI Generated Plugin", version: str = "1.0.0"
) -> str:
    """Creating new project of plugin by Cookiecutter."""
    logger.info(f"Creating project: {plugin_name}")
    
    extra_context = {
        "plugin_name": plugin_name, "author": author, "main_class": main_class,
        "version": version, "description": description,
        "paper_api_version": "1.21.1-R0.1-SNAPSHOT",
        "maven_api_version": "3.13.0", "jdk_version": "25"
    }

    try:
        result_path = cookiecutter(
            TEMPLATE_DIR, no_input=True, extra_context=extra_context,
            output_dir=PROJECTS_DIR, overwrite_if_exists=True
        )
        return f"Success: Project created in {os.path.relpath(result_path, BASE_DIR)}"
    except Exception as e:
        logger.error(f"Cookiecutter Error: {str(e)}")
        return f"Error when created: {str(e)}"

@server.tool()
def write_java_logic(file_path: str, java_code: str) -> str:
    """Writing Java code into project file."""
    clean_p = clean_path_input(file_path)
    full_path = os.path.normpath(os.path.join(PROJECTS_DIR, clean_p))
    
    if not full_path.startswith(os.path.normpath(PROJECTS_DIR)):
        return "Error: Attempt to write out of projects folder was blocked."

    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(java_code)
        logger.info(f"File saved: {clean_p}")
        return f"File {clean_p} was successfully updated."
    except Exception as e:
        return f"Writing error: {str(e)}"

@server.tool()
def build_plugin_jar(plugin_folder_name: str) -> str:
    """Building project by Maven and copying JAR into folder named plugins."""
    clean_folder = clean_path_input(plugin_folder_name)
    project_path = os.path.join(PROJECTS_DIR, clean_folder)
    
    if not os.path.exists(os.path.join(project_path, "pom.xml")):
        return f"Error: In {clean_folder} pom.xml not found"

    try:
        logger.info(f"Executing Maven build for {clean_folder}...")
        # shell=True is critically important in Windows for finding mvn.cmd
        result = subprocess.run(
            ["mvn", "clean", "package", "-DskipTests"],
            cwd=project_path, capture_output=True, text=True, shell=True
        )
        
        if result.returncode != 0:
            return f"Build errors:\n{result.stderr or result.stdout}"

        target_dir = os.path.join(project_path, "target")
        os.makedirs(PLUGINS_DIR, exist_ok=True)
        
        jar_files = [f for f in os.listdir(target_dir) 
                     if f.endswith(".jar") and not any(x in f for x in ["original", "sources", "javadoc"])]
        
        if not jar_files:
            return "Error: JAR wasn't found in folder named target."

        src_jar = os.path.join(target_dir, jar_files[0])
        dest_jar = os.path.join(PLUGINS_DIR, f"{clean_folder}.jar")
        shutil.copy2(src_jar, dest_jar)
        
        return f"Success! Plugin was built and copying into: plugins/{clean_folder}.jar"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    run_self_check()
    server.run()