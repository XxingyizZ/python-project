"""MCP Server：向 Client 提供安全的基础工具。"""

from mcp.server.mcpserver import MCPServer

from tools import calculate as calculate_tool
from tools import list_notes as list_notes_tool
from tools import read_note as read_note_tool


mcp = MCPServer("Python Learning MCP Server")


@mcp.tool()
def calculate(a: float, b: float, operation: str) -> float:
    """执行 add、subtract、multiply 或 divide 四种基础运算。"""
    return calculate_tool(a, b, operation)


@mcp.tool()
def list_notes() -> list[str]:
    """列出可以读取的学习笔记文件名。"""
    return list_notes_tool()


@mcp.tool()
def read_note(note_name: str) -> str:
    """读取白名单中的学习笔记内容。"""
    return read_note_tool(note_name)


if __name__ == "__main__":
    # stdio 是本地 Host 启动 MCP Server 时常用的通信方式。
    # 不要在这里向 stdout 打印普通调试信息，因为 stdout 属于协议通道。
    mcp.run()
