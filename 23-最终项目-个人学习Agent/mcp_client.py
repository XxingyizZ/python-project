"""可选 MCP Client，把 MCP Server 工具转换为本地 Agent 可调用形式。"""

import sys
from pathlib import Path


async def load_mcp_tools(server_path):
    try:
        from mcp import Client, StdioServerParameters
    except ImportError:
        return [], {}, None

    server = StdioServerParameters(command=sys.executable, args=[str(server_path)])
    client = Client(server)
    await client.__aenter__()
    result = await client.list_tools()
    schemas = []
    for tool in result.tools:
        schemas.append({"type": "function", "name": tool.name, "description": tool.description or "MCP工具", "parameters": tool.input_schema})

    async def call(name, arguments):
        response = await client.call_tool(name, arguments)
        return "\n".join(getattr(item, "text", str(item)) for item in response.content)

    return schemas, {tool.name: call for tool in result.tools}, client


async def close_mcp_client(client):
    if client is not None:
        await client.__aexit__(None, None, None)
