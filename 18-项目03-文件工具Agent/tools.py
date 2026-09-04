"""提供受限制的本地学习笔记工具。"""

import json
from pathlib import Path


# __file__是当前Python文件的路径。
# resolve()得到稳定的绝对路径，不依赖用户从哪个目录启动程序。
PROJECT_ROOT = Path(__file__).resolve().parent
NOTES_ROOT = PROJECT_ROOT / "data" / "notes"
ALLOWED_NOTES = ("python.md", "llm.md", "agent.md")


def list_notes():
    """列出允许访问的学习笔记名称。"""
    return list(ALLOWED_NOTES)


def _get_note_path(name):
    """只根据白名单中的文件名取得路径，不接受任意路径。"""
    if not isinstance(name, str):
        raise TypeError("笔记名称必须是字符串。")
    if name not in ALLOWED_NOTES:
        raise ValueError("不允许访问这份笔记。")

    path = NOTES_ROOT / name
    if not path.exists():
        raise FileNotFoundError(f"笔记不存在：{name}")
    if not path.is_file():
        raise ValueError(f"目标不是文件：{name}")
    return path


def read_note(name):
    """读取白名单中的一份Markdown学习笔记。"""
    path = _get_note_path(name)

    try:
        return path.read_text(encoding="utf-8")
    except OSError as e:
        return f"读取笔记失败：{e}"


def search_notes(keyword):
    """在白名单笔记中进行简单的字符串搜索。"""
    if not isinstance(keyword, str):
        raise TypeError("搜索关键词必须是字符串。")
    if not keyword:
        raise ValueError("搜索关键词不能为空。")

    matches = []
    for name in ALLOWED_NOTES:
        content = read_note(name)
        for line_number, line in enumerate(content.splitlines(), start=1):
            if keyword.lower() in line.lower():
                matches.append({
                    "name": name,
                    "line_number": line_number,
                    "content": line,
                })
    return matches


# Tool Schema告诉模型工具名称、用途和参数，而不是把Python函数执行权限交给模型。
TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "list_notes",
        "description": "列出可以访问的学习笔记名称。",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "read_note",
        "description": "读取指定的允许学习笔记，例如python.md。",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "允许的笔记名称"}
            },
            "required": ["name"]
        }
    },
    {
        "type": "function",
        "name": "search_notes",
        "description": "在允许的学习笔记中搜索关键词。",
        "parameters": {
            "type": "object",
            "properties": {
                "keyword": {"type": "string", "description": "要搜索的关键词"}
            },
            "required": ["keyword"]
        }
    }
]


# 工具白名单：模型只能请求这里明确列出的工具。
TOOL_FUNCTIONS = {
    "list_notes": list_notes,
    "read_note": read_note,
    "search_notes": search_notes,
}


def execute_tool(tool_name, arguments):
    """通过白名单执行工具，并返回JSON字符串。"""
    tool = TOOL_FUNCTIONS.get(tool_name)
    if tool is None:
        return json.dumps({"error": f"未知工具：{tool_name}"}, ensure_ascii=False)

    try:
        result = tool(**arguments)
        return json.dumps({"result": result}, ensure_ascii=False)
    except (TypeError, ValueError, FileNotFoundError) as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)
