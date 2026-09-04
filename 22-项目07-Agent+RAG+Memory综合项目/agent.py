"""实现 Agent Loop：模型、工具和工具结果之间的循环。"""

import json

from config import MAX_STEPS
from llm_client import create_response
from memory import add_conversation, memory_context
from tools import TOOL_SCHEMAS, execute_tool


INSTRUCTIONS = """
你是一个 Python 学习助手。
需要查询项目知识时调用 search_knowledge，需要计算时调用 calculate。
需要读取或更新用户信息时调用 Memory 工具。不要编造工具没有返回的事实。
回答要清晰简洁，并说明检索结果中的来源。
""".strip()


def _function_calls(response):
    """从 Responses 输出中找到所有 function_call 项。"""
    return [item for item in response.output if getattr(item, "type", None) == "function_call"]


def run_agent(user_text):
    """运行一次支持多工具调用的 Agent Loop。"""
    if not isinstance(user_text, str) or not user_text.strip():
        raise ValueError("用户问题不能为空。")

    add_conversation("user", user_text)
    input_data = [{"role": "user", "content": f"Memory Context：{memory_context()}\n用户问题：{user_text}"}]
    response = None

    for _ in range(MAX_STEPS):
        response = create_response(
            input_data,
            INSTRUCTIONS,
            TOOL_SCHEMAS,
            getattr(response, "id", None),
        )
        calls = _function_calls(response)
        if not calls:
            answer = response.output_text
            add_conversation("assistant", answer)
            return answer

        # 一个响应可能有多个 function_call，逐个执行后一次性回传。
        outputs = []
        for call in calls:
            try:
                arguments = json.loads(call.arguments)
                result = execute_tool(call.name, arguments)
            except (TypeError, ValueError, json.JSONDecodeError) as error:
                result = json.dumps({"error": str(error)}, ensure_ascii=False)
            outputs.append({"type": "function_call_output", "call_id": call.call_id, "output": result})
        input_data = outputs

    raise RuntimeError("Agent 超过最大工具调用步数。")
