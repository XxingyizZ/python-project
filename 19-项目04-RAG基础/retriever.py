"""实现余弦相似度和Top-K检索。"""

import math


def cosine_similarity(vector_a, vector_b):
    """计算两个向量的余弦相似度。"""
    if len(vector_a) != len(vector_b):
        raise ValueError("两个向量长度不一致。")
    if not vector_a:
        raise ValueError("向量不能为空。")

    length_a = math.sqrt(sum(value * value for value in vector_a))
    length_b = math.sqrt(sum(value * value for value in vector_b))
    if length_a == 0 or length_b == 0:
        return 0.0

    dot_product = sum(a * b for a, b in zip(vector_a, vector_b))
    return dot_product / (length_a * length_b)


def search(query_embedding, chunks, k=3):
    """按相似度排序并返回最相关的K个chunk。"""
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k必须是正整数。")
    if not query_embedding or not chunks:
        return []

    results = []
    for chunk in chunks:
        score = cosine_similarity(query_embedding, chunk["embedding"])
        results.append({
            "source": chunk["source"],
            "text": chunk["text"],
            "score": score,
        })

    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:k]
