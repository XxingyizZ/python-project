"""只负责调用 OpenAI Embeddings API。"""

from config import API_KEY, EMBEDDING_MODEL


def get_embeddings(texts):
    """把多段文本转换成数字向量。"""
    if not texts:
        return []
    if not API_KEY:
        raise ValueError("缺少 OPENAI_API_KEY 环境变量。")
    from openai import OpenAI

    response = OpenAI(api_key=API_KEY).embeddings.create(model=EMBEDDING_MODEL, input=texts)
    return [item.embedding for item in response.data]


def get_embedding(text):
    """把一段文本转换成一个数字向量。"""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Embedding 文本不能为空。")
    return get_embeddings([text])[0]
