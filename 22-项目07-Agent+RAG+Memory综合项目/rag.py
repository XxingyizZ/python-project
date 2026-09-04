"""组织知识库、Embedding、索引和检索，并提供 RAG Tool。"""

import json
from pathlib import Path

from config import TOP_K
from documents import load_chunks
from embeddings import get_embedding, get_embeddings
from retriever import search


INDEX_PATH = Path(__file__).resolve().parent / "data" / "index.json"


def load_index():
    """读取有效 JSON 索引；文件不存在或损坏时返回 None。"""
    if not INDEX_PATH.exists():
        return None
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, list):
        return None
    for chunk in data:
        if not isinstance(chunk, dict) or not all(key in chunk for key in ("source", "text", "embedding")):
            return None
        if not isinstance(chunk["embedding"], list) or not chunk["embedding"]:
            return None
    return data


def save_index(chunks):
    """保存文档 chunk 和向量。"""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(chunks, ensure_ascii=False, indent=2), encoding="utf-8")


def _same_documents(index, chunks):
    return len(index) == len(chunks) and all(
        saved["source"] == current["source"] and saved["text"] == current["text"]
        for saved, current in zip(index, chunks)
    )


def build_or_load_index():
    """加载仍然有效的索引，否则调用 Embeddings API 重建。"""
    chunks = load_chunks()
    if not chunks:
        raise ValueError("知识库中没有可用文档。")
    index = load_index()
    if index is not None and _same_documents(index, chunks):
        return index
    vectors = get_embeddings([chunk["text"] for chunk in chunks])
    if len(vectors) != len(chunks):
        raise ValueError("Embedding 数量与 chunk 数量不一致。")
    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector
    save_index(chunks)
    return chunks


def search_knowledge(query):
    """RAG Tool：检索知识并返回来源、文本和相似度。"""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("检索问题不能为空。")
    index = build_or_load_index()
    results = search(get_embedding(query), index, TOP_K)
    return results


def build_context(results):
    """把检索结果整理成模型可以阅读的上下文。"""
    return "\n\n".join(
        f"来源：{item['source']}\n相似度：{item['score']:.4f}\n内容：{item['text']}"
        for item in results
    )
