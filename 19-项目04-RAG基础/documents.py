"""读取和切分知识文档。"""

from pathlib import Path

from config import CHUNK_OVERLAP, CHUNK_SIZE


KNOWLEDGE_ROOT = Path(__file__).resolve().parent / "data" / "knowledge"


def load_documents():
    """读取知识目录中的Markdown文档。"""
    documents = []
    for path in sorted(KNOWLEDGE_ROOT.glob("*.md")):
        documents.append({
            "source": path.name,
            "text": path.read_text(encoding="utf-8"),
        })
    return documents


def chunk_text(text, source, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """按固定字符数切分文本，并保留来源。"""
    if not isinstance(text, str) or not text:
        return []
    if chunk_size < 1 or chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("chunk_size和chunk_overlap参数无效。")

    chunks = []
    start = 0
    step = chunk_size - chunk_overlap
    while start < len(text):
        end = start + chunk_size
        chunks.append({"source": source, "text": text[start:end]})
        start += step
    return chunks


def load_chunks():
    """读取全部文档并切分为chunk。"""
    chunks = []
    for document in load_documents():
        chunks.extend(chunk_text(document["text"], document["source"]))
    return chunks
