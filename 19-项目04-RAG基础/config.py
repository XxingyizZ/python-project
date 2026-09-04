"""RAG项目的简单配置。"""

import os


API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-5.6")
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

try:
    TOP_K = int(os.getenv("RAG_TOP_K", "3"))
except ValueError:
    TOP_K = 3

try:
    CHUNK_SIZE = int(os.getenv("RAG_CHUNK_SIZE", "300"))
except ValueError:
    CHUNK_SIZE = 300

try:
    CHUNK_OVERLAP = int(os.getenv("RAG_CHUNK_OVERLAP", "50"))
except ValueError:
    CHUNK_OVERLAP = 50

TOP_K = max(TOP_K, 1)
CHUNK_SIZE = max(CHUNK_SIZE, 1)
CHUNK_OVERLAP = max(min(CHUNK_OVERLAP, CHUNK_SIZE - 1), 0)
