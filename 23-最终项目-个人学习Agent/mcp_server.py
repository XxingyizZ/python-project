"""可选的本地 MCP Server；没有安装 mcp 时不会影响核心项目。"""

from pathlib import Path


def run_server():
    try:
        from mcp.server import MCPServer
    except ImportError as error:
        raise RuntimeError("MCP SDK 未安装。") from error

    root = Path(__file__).resolve().parent / "data" / "knowledge"
    server = MCPServer("Personal Learning MCP Server")

    @server.tool()
    def list_notes() -> list[str]:
        """列出学习笔记。"""
        return [path.name for path in sorted(root.glob("*.md"))]

    @server.tool()
    def read_note(note_name: str) -> str:
        """读取知识库中的固定笔记。"""
        allowed = {path.name: path for path in root.glob("*.md")}
        if note_name not in allowed:
            raise ValueError("只能读取知识库中的笔记。")
        return allowed[note_name].read_text(encoding="utf-8")

    server.run()


if __name__ == "__main__":
    run_server()
