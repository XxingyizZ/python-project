"""读取和切分知识库文档。"""

from pathlib import Path

from config import CHUNK_OVERLAP, CHUNK_SIZE


KNOWLEDGE_ROOT = Path(__file__).resolve().parent / "data" / "knowledge"


def load_documents():
    """只读取项目知识库目录中的 Markdown 文件。"""
    documents = []
    for path in sorted(KNOWLEDGE_ROOT.glob("*.md")):
        documents.append({"source": path.name, "text": path.read_text(encoding="utf-8")})
    return documents


def chunk_text(text, source, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    """按固定字符数切分文本，并保留来源。"""
    if not isinstance(text, str) or not text:
        return []
    if chunk_size < 1 or chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError("chunk_size 或 chunk_overlap 参数无效。")
    chunks = []
    start = 0
    step = chunk_size - chunk_overlap
    while start < len(text):
        chunks.append({"source": source, "text": text[start:start + chunk_size]})
        start += step
    return chunks


def load_chunks():
    """读取全部知识文档并切分。"""
    chunks = []
    for document in load_documents():
        chunks.extend(chunk_text(document["text"], document["source"]))
    return chunks
