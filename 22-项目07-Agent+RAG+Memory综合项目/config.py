"""综合 Agent 项目的简单配置。"""

import os


API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-5.6")
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")


def _read_positive_int(name, default):
    """读取正整数配置，配置错误时使用默认值。"""
    try:
        return max(int(os.getenv(name, str(default))), 1)
    except ValueError:
        return default


MAX_STEPS = _read_positive_int("AGENT_MAX_STEPS", 5)
MAX_HISTORY = _read_positive_int("MAX_HISTORY", 10)
TOP_K = _read_positive_int("RAG_TOP_K", 3)
CHUNK_SIZE = _read_positive_int("RAG_CHUNK_SIZE", 300)
CHUNK_OVERLAP = max(min(_read_positive_int("RAG_CHUNK_OVERLAP", 50), CHUNK_SIZE - 1), 0)
