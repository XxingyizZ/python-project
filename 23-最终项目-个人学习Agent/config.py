"""集中管理最终项目的配置。"""

import os
from pathlib import Path


API_KEY = os.getenv("OPENAI_API_KEY")
CHAT_MODEL = os.getenv("OPENAI_CHAT_MODEL", "gpt-5.6")
EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")
ENABLE_MCP = os.getenv("ENABLE_MCP", "false").lower() == "true"
PROJECT_DIR = Path(__file__).resolve().parent
MCP_SERVER_PATH = PROJECT_DIR / "mcp_server.py"


def _positive_int(name, default):
    try:
        return max(int(os.getenv(name, str(default))), 1)
    except ValueError:
        return default


MAX_STEPS = _positive_int("AGENT_MAX_STEPS", 5)
MAX_HISTORY = _positive_int("MAX_HISTORY", 10)
TOP_K = _positive_int("RAG_TOP_K", 3)
CHUNK_SIZE = _positive_int("RAG_CHUNK_SIZE", 300)
CHUNK_OVERLAP = min(_positive_int("RAG_CHUNK_OVERLAP", 50), CHUNK_SIZE - 1)
