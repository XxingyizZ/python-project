"""实现使用Memory Tool的Agent Loop。"""

import json

from config import MAX_STEPS
from llm_client import create_response
from memory import add_conversation, get_memory, update_memory


TOOL_SCHEMAS = [
    {
        "type": "function",
        "name": "get_memory",
        "description": "读取用户的姓名和学习目标等长期Memory。",
        "parameters": {"type": "object", "properties": {}, "required": []},
    },
    {
        "type": "function",
        "name": "update_memory",
        "description": "更新用户姓名或学习目标。只能修改name和learning_goal。",
        "parameters": {
            "type": "object",
            "properties": {
                "key": {
                    "type": "string",
                    "enum": ["name", "learning_goal"],
                    "description": "允许修改的Memory字段",
                },
                "value": {"type": "string", "description": "要保存的内容"},
            },
            "required": ["key", "value"],
        },
    },
]


def build_memory_context(memory):
    """把适合提供给模型的Memory整理成上下文。"""
    user = memory["user"]
    context = [
        f"用户姓名：{user['name'] or '未知'}",
        f"学习目标：{user['learning_goal'] or '未知'}",
    ]
    if memory["conversation"]:
        context.append("最近对话：")
        for item in memory["conversation"]:
            context.append(f"{item['role']}：{item['content']}")
    return "\n".join(context)


def execute_memory_tool(tool_name, arguments):
    """执行白名单中的Memory工具。"""
    if tool_name == "get_memory":
        return get_memory()
    if tool_name == "update_memory":
        return update_memory(arguments["key"], arguments["value"])
    raise ValueError(f"未知Memory工具：{tool_name}")


def run_agent(user_text, previous_response_id=None):
    """运行一次Memory Agent任务，并返回回答和响应ID。"""
    memory = get_memory()
    prompt = (
        "以下是应用从持久化Memory中整理出的上下文：\n"
        f"{build_memory_context(memory)}\n\n"
        "请根据当前用户输入回答。如果用户明确提供姓名或学习目标，"
        "可以使用update_memory保存。当前用户输入：\n"
        f"{user_text}"
    )
    input_items = [{"role": "user", "content": prompt}]

    for step in range(MAX_STEPS):
        response = create_response(
            input_items,
            TOOL_SCHEMAS,
            previous_response_id=previous_response_id if step == 0 else None,
        )
        input_items += response.output
        function_calls = [
            item for item in response.output if item.type == "function_call"
        ]

        if not function_calls:
            answer = response.output_text
            add_conversation("user", user_text)
            add_conversation("assistant", answer)
            return answer, response.id

        for item in function_calls:
            try:
                arguments = json.loads(item.arguments)
                result = execute_memory_tool(item.name, arguments)
                output = json.dumps(result, ensure_ascii=False)
            except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError) as e:
                output = json.dumps({"error": str(e)}, ensure_ascii=False)

            input_items.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": output,
            })

    return "Agent达到最大执行步数，已停止本次任务。", None
