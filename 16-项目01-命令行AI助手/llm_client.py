"""封装OpenAI Responses API调用。"""

from openai import OpenAI

from config import MODEL, get_api_key


def ask_llm(user_text, previous_response_id=None):
    """向模型发送一轮输入，并返回文本和本轮响应ID。"""
    api_key = get_api_key()
    if not api_key:
        raise ValueError("缺少OPENAI_API_KEY环境变量。")

    # OpenAI SDK会使用API Key创建客户端。
    client = OpenAI(api_key=api_key)

    request_data = {
        "model": MODEL,
        "input": user_text,
    }

    # previous_response_id让当前请求继续上一轮对话。
    if previous_response_id:
        request_data["previous_response_id"] = previous_response_id

    response = client.responses.create(**request_data)
    return response.output_text, response.id
