$ROOT_DIR = Resolve-Path "$PSScriptRoot\.."
$TEMPLATE_DIR = "$ROOT_DIR\template"
$PROJECT_DIR = "$ROOT_DIR\projects"
New-Item -ItemType Directory -Force -Path $PROJECT_DIR | Out-Null

Write-Host "=== Paper Plugin Generator (Windows PS) ===" -ForegroundColor Cyan

# -------------------------
# 1. User defined data
# -------------------------
$PLUGIN_NAME = Read-Host "Plugin name [myplugin]"
if (-not $PLUGIN_NAME) { $PLUGIN_NAME = "myplugin" }

$AUTHOR = Read-Host "Author [myname]"
if (-not $AUTHOR) { $AUTHOR = "myname" }

$MAIN_CLASS = Read-Host "Main class [MyPlugin]"
if (-not $MAIN_CLASS) { $MAIN_CLASS = "MyPlugin" }

$VERSION = Read-Host "Version [1.0.0]"
if (-not $VERSION) { $VERSION = "1.0.0" }

$API_VERSION = Read-Host "Paper API version [1.21.1-R0.1-SNAPSHOT]"
if (-not $API_VERSION) { $API_VERSION = "1.21.1-R0.1-SNAPSHOT" }

$MAVEN_API_VERSION = Read-Host "Maven API version [3.13.0]"
if (-not $MAVEN_API_VERSION) { $MAVEN_API_VERSION = "3.13.0" }

$JDK_VERSION = Read-Host "OpenJDK API version [25]"
if (-not $JDK_VERSION) {$JDK_VERSION = "25"}

$DESCRIPTION = Read-Host "Description [example]"
if (-not $DESCRIPTION) { $DESCRIPTION = "example"}

# -------------------------
# 2. Creating project structure by cookiecutter in plugins
# -------------------------
python -m cookiecutter "$TEMPLATE_DIR" `
  --no-input `
  --output-dir "$PROJECT_DIR" `
  plugin_name="$PLUGIN_NAME" `
  author="$AUTHOR" `
  main_class="$MAIN_CLASS" `
  version="$VERSION" `
  paper_api_version="$API_VERSION" `
  maven_api_version="$MAVEN_API_VERSION" `
  jdk_version="$JDK_VERSION" `
  description="$DESCRIPTION"