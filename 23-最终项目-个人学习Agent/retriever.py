"""标准库实现余弦相似度和 Top-K。"""

import math


def cosine_similarity(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("向量长度不一致。")
    if not vector_a:
        raise ValueError("向量不能为空。")
    length_a = math.sqrt(sum(value * value for value in vector_a))
    length_b = math.sqrt(sum(value * value for value in vector_b))
    if length_a == 0 or length_b == 0:
        return 0.0
    return sum(a * b for a, b in zip(vector_a, vector_b)) / (length_a * length_b)


def search(query_embedding, chunks, k=3):
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k 必须是正整数。")
    if not query_embedding or not chunks:
        return []
    results = [{"source": c["source"], "text": c["text"], "score": cosine_similarity(query_embedding, c["embedding"])} for c in chunks]
    results.sort(key=lambda item: item["score"], reverse=True)
    return results[:k]
