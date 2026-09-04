"""定义Agent可以使用的安全Python工具。"""

import json


def calculate(a, b, operation):
    """执行有限的四则运算，不执行任意代码。"""
    if isinstance(a, bool) or not isinstance(a, (int, float)):
        raise TypeError("a必须是数字。")
    if isinstance(b, bool) or not isinstance(b, (int, float)):
        raise TypeError("b必须是数字。")

    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide":
        if b == 0:
            raise ValueError("除数不能为0。")
        return a / b

    raise ValueError("operation必须是add、subtract、multiply或divide。")


def get_learning_record():
    """返回写在程序内存中的示例学习记录。"""
    return {
        "completed": ["Python核心语法", "数据容器", "函数"],
        "current": "Function Tool Agent",
        "next": "更复杂的Agent项目",
    }


# Tool Schema告诉模型工具能做什么以及需要哪些参数。
TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "calculate",
        "description": "执行有限的基础数学运算。",
        "parameters": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "第一个数字"},
                "b": {"type": "number", "description": "第二个数字"},
                "operation": {
                    "type": "string",
                    "enum": ["add", "subtract", "multiply", "divide"],
                    "description": "要执行的运算"
                }
            },
            "required": ["a", "b", "operation"]
        }
    },
    {
        "type": "function",
        "name": "get_learning_record",
        "description": "查询当前程序中的示例学习记录。",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    }
]


# 明确的工具白名单，不根据模型字符串动态执行函数。
TOOL_FUNCTIONS = {
    "calculate": calculate,
    "get_learning_record": get_learning_record,
}


def execute_tool(tool_name, arguments):
    """根据白名单执行工具，并返回可传给模型的字符串结果。"""
    tool = TOOL_FUNCTIONS.get(tool_name)
    if tool is None:
        return json.dumps({"error": f"未知工具：{tool_name}"}, ensure_ascii=False)

    try:
        result = tool(**arguments)
        return json.dumps({"result": result}, ensure_ascii=False)
    except (TypeError, ValueError) as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)
