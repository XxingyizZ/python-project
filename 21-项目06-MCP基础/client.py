"""MCP Client：通过 stdio 发现并调用本地 MCP Server。"""

from mcp import Client, StdioServerParameters

from config import PYTHON_COMMAND, get_server_path


def _print_tool_result(title, result):
    """打印 MCP 调用结果，便于观察 Client 收到的内容。"""
    print(title)
    if getattr(result, "is_error", False):
        print("工具执行失败：", result)
        return

    for content in result.content:
        text = getattr(content, "text", None)
        print(text if text is not None else content)


async def run_client():
    """启动 Server，发现工具并调用三个示例工具。"""
    server = StdioServerParameters(
        command=PYTHON_COMMAND,
        args=[str(get_server_path())],
    )

    # async with 负责建立会话，并在离开代码块时关闭连接和子进程。
    async with Client(server) as client:
        tool_result = await client.list_tools()
        print("已发现工具：")
        for tool in tool_result.tools:
            print(f"- {tool.name}：{tool.description}")
            print(f"  输入结构：{tool.input_schema}")

        result = await client.call_tool(
            "calculate",
            {"a": 10, "b": 20, "operation": "add"},
        )
        _print_tool_result("计算结果：", result)

        result = await client.call_tool("list_notes", {})
        _print_tool_result("笔记列表：", result)

        result = await client.call_tool("read_note", {"note_name": "mcp.md"})
        _print_tool_result("mcp.md 内容：", result)
