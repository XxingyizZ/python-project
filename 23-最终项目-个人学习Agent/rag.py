"""RAG：文档、索引、Embedding 和检索。"""

import json
from pathlib import Path

from config import TOP_K
from documents import load_chunks
from embeddings import get_embedding, get_embeddings
from retriever import search


INDEX_PATH = Path(__file__).resolve().parent / "data" / "index.json"


def load_index():
    if not INDEX_PATH.exists():
        return None
    try:
        data = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(data, list):
        return None
    for item in data:
        if not isinstance(item, dict) or not all(key in item for key in ("source", "text", "embedding")) or not item["embedding"]:
            return None
    return data


def save_index(data):
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def build_or_load_index():
    chunks = load_chunks()
    if not chunks:
        raise ValueError("知识库为空。")
    index = load_index()
    if index and len(index) == len(chunks) and all(a["source"] == b["source"] and a["text"] == b["text"] for a, b in zip(index, chunks)):
        return index
    vectors = get_embeddings([item["text"] for item in chunks])
    for chunk, vector in zip(chunks, vectors):
        chunk["embedding"] = vector
    save_index(chunks)
    return chunks


def search_knowledge(query):
    if not isinstance(query, str) or not query.strip():
        raise ValueError("检索问题不能为空。")
    return search(get_embedding(query), build_or_load_index(), TOP_K)
