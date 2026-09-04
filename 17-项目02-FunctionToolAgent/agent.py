"""实现最基本的Function Tool Agent Loop。"""

import json

from config import MAX_STEPS
from llm_client import create_response
from tools import TOOL_SCHEMAS, execute_tool


def run_agent(user_text):
    """运行一次Agent任务，直到模型回答或达到最大步数。"""
    input_items = [{"role": "user", "content": user_text}]

    for step in range(MAX_STEPS):
        response = create_response(input_items, TOOL_SCHEMAS)

        # 保存模型输出，下一轮请求需要知道之前发生了什么。
        input_items += response.output
        function_calls = []

        for item in response.output:
            if item.type == "function_call":
                function_calls.append(item)

        if not function_calls:
            return response.output_text

        # 一次响应可能包含多个function_call，逐个执行后一起回传。
        for item in function_calls:
            try:
                arguments = json.loads(item.arguments)
                output = execute_tool(item.name, arguments)
            except json.JSONDecodeError:
                output = json.dumps({"error": "工具参数不是有效JSON。"}, ensure_ascii=False)

            input_items.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": output,
            })

    return "Agent达到最大执行步数，已停止本次任务。"
