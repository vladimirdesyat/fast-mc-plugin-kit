# MCP Server Configuration Example

To use **fast-mc-plugin-kit** with an AI, you need to register the `mcp/server.py` in your favorite MCP client.

## LM Studio (Local AI)
Go to the **My Tools** or **MCP** section in LM Studio and add a new local server with this configuration:

```json
{
  "mcpServers": {
    "fast-mc-kit": {
      "command": "python",
      "args": ["C:/fast-mc-plugin-kit/mcp/server.py"],
      "env": {
        "PYTHONPATH": "C:/fast-mc-plugin-kit"
      }
    }
  }
}
```
## Tip: To get the absolute path for your config, run this in your terminal inside the project folder:
- Windows (PowerShell): (Get-Item .\mcp\server.py).FullName
- Mac/Linux: readlink -f mcp/server.py