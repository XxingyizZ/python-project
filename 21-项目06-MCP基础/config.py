"""集中管理 MCP 基础项目的简单配置。"""

import os
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent


def get_server_path():
    """获取 MCP Server 路径，默认使用当前项目的 server.py。"""
    configured_path = os.getenv("MCP_SERVER_PATH")
    if configured_path:
        server_path = Path(configured_path)
        if not server_path.is_absolute():
            server_path = PROJECT_DIR / server_path
        return server_path.resolve()

    return PROJECT_DIR / "server.py"


PYTHON_COMMAND = sys.executable
