"""封装OpenAI Responses API调用。"""

from openai import OpenAI

from config import API_KEY, MODEL


def create_response(input_items, tools, previous_response_id=None):
    """把上下文和工具描述发送给模型。"""
    if not API_KEY:
        raise ValueError("缺少OPENAI_API_KEY环境变量。")

    request_data = {
        "model": MODEL,
        "input": input_items,
        "tools": tools,
    }
    if previous_response_id:
        request_data["previous_response_id"] = previous_response_id

    client = OpenAI(api_key=API_KEY)
    return client.responses.create(**request_data)
