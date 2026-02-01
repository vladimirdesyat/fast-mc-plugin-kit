## Example Interaction: "The Teleport Stick"
- This example demonstrates how a user should interact with the AI to trigger the full automation pipeline.

## User Query:
- "I want to create a plugin called 'MagicStick'. It should give players a stick that teleports them 5 blocks forward when they left-click. Check my env, create the project, write the code, and build the jar."

## AI Internal Workflow (The "Chain of Thought"):
- Call check_environment:
    - Output: "Java 25, Maven 3.13, and Cookiecutter detected."

## Call create_new_plugin:
- Arguments: plugin_name="MagicStick", package_name="me.dev.magicstick"
- Output: "Project created at /projects/MagicStick."

## Call write_java_logic:
- Path: MagicStick/src/main/java/me/dev/magicstick/MagicStick.java
- Logic: Implement PlayerInteractEvent, check for Action.LEFT_CLICK_AIR, and use player.teleport().

## Call build_plugin_jar:
- Arguments: plugin_folder_name="MagicStick"
- Output: "Build Success! JAR moved to /plugins/MagicStick.jar."

## Expected AI Response:
- "I've completed your request for MagicStick:
    - Environment: Verified and ready.
    - Scaffolding: Created a new project structure in projects/MagicStick.
    - Implementation: I wrote the teleportation logic using the Bukkit API.
    - Build: The plugin was compiled successfully.
    - You can now find MagicStick.jar in your plugins folder. Ready to install on your server!"