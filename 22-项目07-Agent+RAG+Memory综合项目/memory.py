"""读取、保存和更新 JSON Memory。"""

import json
from pathlib import Path

from config import MAX_HISTORY


MEMORY_PATH = Path(__file__).resolve().parent / "data" / "memory.json"
ALLOWED_KEYS = {"name", "learning_goal"}


def _default_memory():
    return {"user": {"name": "", "learning_goal": ""}, "facts": [], "conversation": []}


def _validate_memory(memory):
    if not isinstance(memory, dict) or not isinstance(memory.get("user"), dict):
        raise ValueError("Memory结构无效。")
    if not all(key in memory["user"] for key in ALLOWED_KEYS):
        raise ValueError("Memory缺少必要字段。")
    if not isinstance(memory.get("facts"), list) or not isinstance(memory.get("conversation"), list):
        raise ValueError("Memory中的列表字段无效。")


def load_memory():
    """读取 Memory；文件不存在时返回初始结构。"""
    if not MEMORY_PATH.exists():
        return _default_memory()
    try:
        memory = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("memory.json 不是有效 JSON。") from error
    except OSError as error:
        raise OSError(f"读取 Memory 失败：{error}") from error
    _validate_memory(memory)
    return memory


def save_memory(memory):
    """验证后保存 Memory。"""
    _validate_memory(memory)
    try:
        MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
        MEMORY_PATH.write_text(json.dumps(memory, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError as error:
        raise OSError(f"保存 Memory 失败：{error}") from error


def get_memory():
    """返回当前 Memory。"""
    return load_memory()


def update_memory(key, value):
    """只更新允许的用户字段。"""
    if key not in ALLOWED_KEYS:
        raise ValueError("只允许更新 name 或 learning_goal。")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Memory 内容不能为空。")
    memory = load_memory()
    memory["user"][key] = value.strip()
    memory["facts"] = [item for item in memory["facts"] if item.get("key") != key]
    memory["facts"].append({"key": key, "value": value.strip()})
    save_memory(memory)
    return memory


def add_conversation(role, content):
    """保存对话，并只保留最近有限条记录。"""
    if role not in {"user", "assistant"}:
        raise ValueError("对话 role 必须是 user 或 assistant。")
    if not isinstance(content, str) or not content.strip():
        raise ValueError("对话内容不能为空。")
    memory = load_memory()
    memory["conversation"].append({"role": role, "content": content})
    memory["conversation"] = memory["conversation"][-MAX_HISTORY:]
    save_memory(memory)
    return memory


def memory_context():
    """构建简短上下文，不把整个 JSON 文件交给模型。"""
    user = load_memory()["user"]
    parts = []
    if user["name"]:
        parts.append(f"用户姓名：{user['name']}")
    if user["learning_goal"]:
        parts.append(f"学习目标：{user['learning_goal']}")
    return "；".join(parts) if parts else "暂无已保存的用户信息。"
