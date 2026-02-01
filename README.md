# Tiny Minecraft Plugin Toolkit

A small, practical toolkit for quickly creating and building Paper/Bukkit
Minecraft server plugins.

## What it does
- Generates a Java plugin project from a template using Cookiecutter
- Builds plugins with Maven
- Collects resulting JARs into a `plugins` directory
- Uses simple PowerShell scripts (no Docker, no magic)

## What it is not
- Not a framework
- Not an IDE replacement
- ~~Not an AI-powered generator (yet)~~ Now AI-Ready via MCP!

## AI Capabilities (MCP Server)
The toolkit now includes a Model Context Protocol (MCP) server. This allows AI models (like Claude, GPT-4, or local models in LM Studio) to:
- Check your local environment for Java/Maven.
- Scaffold new plugins using the included templates.
- Write Java logic directly into your project files.
- Compile the project into a JAR automatically.
- To use it, point your MCP-compatible client to mcp/server.py.

## Requirements
- Python 3.x
- Cookiecutter
- Java (JDK)
- Maven

## Python dependencies (optional):
pip install -r requirements.txt

## Philosophy
Minimal automation, predictable structure, manual control where it matters.