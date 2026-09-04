"""MCP Server 使用的安全本地工具。"""

from pathlib import Path


NOTES_DIR = Path(__file__).resolve().parent / "data" / "notes"
NOTE_NAMES = ("python.md", "agent.md", "mcp.md")


def calculate(a, b, operation):
    """执行有限的基础运算，不执行任意代码。"""
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a 必须是数字。")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b 必须是数字。")

    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("除数不能为 0。")
        return a / b

    raise ValueError("operation 必须是 add、subtract、multiply 或 divide。")


def list_notes():
    """返回允许读取的笔记文件名。"""
    return list(NOTE_NAMES)


def _get_note_path(note_name):
    """只返回白名单中的笔记路径，拒绝任意路径。"""
    if not isinstance(note_name, str) or note_name not in NOTE_NAMES:
        raise ValueError("只能读取白名单中的笔记文件。")

    note_path = NOTES_DIR / note_name
    if not note_path.is_file():
        raise FileNotFoundError(f"笔记不存在：{note_name}")
    return note_path


def read_note(note_name):
    """读取白名单中的一份学习笔记。"""
    return _get_note_path(note_name).read_text(encoding="utf-8")
