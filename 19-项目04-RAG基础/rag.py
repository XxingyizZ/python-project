"""组织完整的RAG流程。"""

import json
from pathlib import Path

from config import TOP_K
from documents import load_chunks
from embeddings import get_embedding, get_embeddings
from llm_client import generate_answer
from retriever import search


INDEX_PATH = Path(__file__).resolve().parent / "data" / "index.json"


def save_index(chunks):
    """把chunk和向量保存到JSON文件。"""
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load_index():
    """读取JSON索引；文件不存在或损坏时返回None。"""
    if not INDEX_PATH.exists():
        return None

    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None

    if not isinstance(data, list):
        return None
    for chunk in data:
        if not isinstance(chunk, dict):
            return None
        if not all(key in chunk for key in ("source", "text", "embedding")):
            return None
        if not isinstance(chunk["embedding"], list) or not chunk["embedding"]:
            return None
    return data


def _same_documents(index, chunks):
    """检查索引中的来源和文本是否仍与知识文档一致。"""
    if len(index) != len(chunks):
        return False
    return all(
        saved["source"] == current["source"]
        and saved["text"] == current["text"]
        for saved, current in zip(index, chunks)
    )


def build_or_load_index():
    """加载有效索引，否则重新生成Embedding并保存。"""
    chunks = load_chunks()
    if not chunks:
        raise ValueError("知识库中没有可用文档。")

    index = load_index()
    if index is not None and _same_documents(index, chunks):
        return index

    vectors = get_embeddings([chunk["text"] for chunk in chunks])
    if len(vectors) != len(chunks):
        raise ValueError("Embedding数量与chunk数量不一致。")

    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector
    save_index(chunks)
    return chunks


def build_context(results):
    """把Top-K检索结果整理为模型上下文。"""
    parts = []
    for result in results:
        parts.append(
            f"来源：{result['source']}\n"
            f"相似度：{result['score']:.4f}\n"
            f"内容：{result['text']}"
        )
    return "\n\n".join(parts)


def answer_question(question):
    """执行问题Embedding、检索、上下文构建和回答生成。"""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("问题不能为空。")

    index = build_or_load_index()
    query_embedding = get_embedding(question)
    results = search(query_embedding, index, TOP_K)
    if not results:
        return "知识库中没有找到相关内容。"

    return generate_answer(question, build_context(results))
