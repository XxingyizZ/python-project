"""加载和切分固定知识库。"""

from pathlib import Path

from config import CHUNK_OVERLAP, CHUNK_SIZE


KNOWLEDGE_ROOT = Path(__file__).resolve().parent / "data" / "knowledge"


def load_documents():
    return [{"source": path.name, "text": path.read_text(encoding="utf-8")} for path in sorted(KNOWLEDGE_ROOT.glob("*.md"))]


def chunk_text(text, source, chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP):
    if not isinstance(text, str) or not text:
        return []
    if chunk_size < 1 or not 0 <= chunk_overlap < chunk_size:
        raise ValueError("chunk 参数无效。")
    chunks = []
    step = chunk_size - chunk_overlap
    for start in range(0, len(text), step):
        chunks.append({"source": source, "text": text[start:start + chunk_size]})
    return chunks


def load_chunks():
    chunks = []
    for document in load_documents():
        chunks.extend(chunk_text(document["text"], document["source"]))
    return chunks
