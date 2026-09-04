"""调用OpenAI Responses API生成回答。"""

from openai import OpenAI

from config import API_KEY, CHAT_MODEL


def generate_answer(question, context):
    """根据用户问题和检索上下文生成回答。"""
    if not API_KEY:
        raise ValueError("缺少OPENAI_API_KEY环境变量。")

    instructions = (
        "你是一个学习助手。请优先根据提供的知识库上下文回答问题。"
        "如果上下文没有相关信息，请明确说明知识库中没有找到相关内容。"
    )
    prompt = f"知识库上下文：\n{context}\n\n用户问题：\n{question}"

    client = OpenAI(api_key=API_KEY)
    response = client.responses.create(
        model=CHAT_MODEL,
        instructions=instructions,
        input=prompt,
    )
    return response.output_text
