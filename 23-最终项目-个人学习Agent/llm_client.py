"""只负责调用 Responses API。"""

from config import API_KEY, CHAT_MODEL


def create_response(input_data, instructions, tools, previous_response_id=None):
    if not API_KEY:
        raise ValueError("缺少 OPENAI_API_KEY 环境变量。")
    from openai import OpenAI
    request = {"model": CHAT_MODEL, "instructions": instructions, "input": input_data, "tools": tools}
    if previous_response_id:
        request["previous_response_id"] = previous_response_id
    return OpenAI(api_key=API_KEY).responses.create(**request)
