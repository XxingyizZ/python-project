"""本地 Function Tool、Tool Schema 和安全白名单。"""

import json

from memory import get_memory, update_memory
from rag import search_knowledge


def calculate(a, b, operation):
    if isinstance(a, bool) or not isinstance(a, (int, float)) or isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("a 和 b 必须是数字。")
    if operation == "add": return a + b
    if operation == "subtract": return a - b
    if operation == "multiply": return a * b
    if operation == "divide":
        if b == 0: raise ValueError("除数不能为 0。")
        return a / b
    raise ValueError("operation 必须是 add、subtract、multiply 或 divide。")


def get_learning_status():
    return {"completed": ["Python基础", "数据容器", "函数", "Agent基础"], "current": "个人学习Agent", "next": "继续完成项目实践"}


TOOL_SCHEMAS = [
    {"type": "function", "name": "calculate", "description": "执行有限的四则运算。", "parameters": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}, "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]}}, "required": ["a", "b", "operation"], "additionalProperties": False}},
    {"type": "function", "name": "get_memory", "description": "读取用户姓名和学习目标。", "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False}},
    {"type": "function", "name": "update_memory", "description": "更新用户姓名或学习目标。", "parameters": {"type": "object", "properties": {"key": {"type": "string", "enum": ["name", "learning_goal"]}, "value": {"type": "string"}}, "required": ["key", "value"], "additionalProperties": False}},
    {"type": "function", "name": "search_knowledge", "description": "检索个人学习知识库。", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"], "additionalProperties": False}},
    {"type": "function", "name": "get_learning_status", "description": "查看学习进度。", "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False}},
]

LOCAL_TOOLS = {"calculate": calculate, "get_memory": get_memory, "update_memory": update_memory, "search_knowledge": search_knowledge, "get_learning_status": get_learning_status}


def execute_local_tool(name, arguments):
    tool = LOCAL_TOOLS.get(name)
    if tool is None: return json.dumps({"error": f"未知本地工具：{name}"}, ensure_ascii=False)
    try: return json.dumps({"result": tool(**arguments)}, ensure_ascii=False)
    except (TypeError, ValueError, OSError) as error: return json.dumps({"error": str(error)}, ensure_ascii=False)
