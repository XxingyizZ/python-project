"""Agent 可调用工具的白名单和工具 Schema。"""

import json

from memory import get_memory, update_memory
from rag import search_knowledge


def calculate(a, b, operation):
    """执行有限的四则运算，不执行任意代码。"""
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


TOOL_SCHEMAS = [
    {"type": "function", "name": "calculate", "description": "执行有限的基础数学运算。", "parameters": {"type": "object", "properties": {"a": {"type": "number"}, "b": {"type": "number"}, "operation": {"type": "string", "enum": ["add", "subtract", "multiply", "divide"]}}, "required": ["a", "b", "operation"], "additionalProperties": False}},
    {"type": "function", "name": "get_memory", "description": "读取当前保存的用户信息。", "parameters": {"type": "object", "properties": {}, "required": [], "additionalProperties": False}},
    {"type": "function", "name": "update_memory", "description": "更新用户姓名或学习目标。", "parameters": {"type": "object", "properties": {"key": {"type": "string", "enum": ["name", "learning_goal"]}, "value": {"type": "string"}}, "required": ["key", "value"], "additionalProperties": False}},
    {"type": "function", "name": "search_knowledge", "description": "从项目知识库检索与问题相关的内容。", "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"], "additionalProperties": False}},
]


TOOL_FUNCTIONS = {"calculate": calculate, "get_memory": get_memory, "update_memory": update_memory, "search_knowledge": search_knowledge}


def execute_tool(tool_name, arguments):
    """根据白名单执行工具，并将结果编码成 JSON 字符串。"""
    tool = TOOL_FUNCTIONS.get(tool_name)
    if tool is None:
        return json.dumps({"error": f"未知工具：{tool_name}"}, ensure_ascii=False)
    try:
        result = tool(**arguments)
        return json.dumps({"result": result}, ensure_ascii=False)
    except (TypeError, ValueError, OSError) as error:
        return json.dumps({"error": str(error)}, ensure_ascii=False)
