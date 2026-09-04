"""只负责调用 OpenAI Responses API。"""

from config import API_KEY, CHAT_MODEL


def create_response(input_data, instructions, tools=None, previous_response_id=None):
    """创建一次 Responses 请求，不把 Agent、RAG 或 Memory 逻辑放在这里。"""
    if not API_KEY:
        raise ValueError("缺少 OPENAI_API_KEY 环境变量。")
    from openai import OpenAI

    request = {
        "model": CHAT_MODEL,
        "instructions": instructions,
        "input": input_data,
        "tools": tools or [],
    }
    if previous_response_id:
        request["previous_response_id"] = previous_response_id
    return OpenAI(api_key=API_KEY).responses.create(**request)
