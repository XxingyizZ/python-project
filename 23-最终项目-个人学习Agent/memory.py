"""JSON 持久化 Memory。"""

import json
from pathlib import Path

from config import MAX_HISTORY


MEMORY_PATH = Path(__file__).resolve().parent / "data" / "memory.json"
ALLOWED_KEYS = {"name", "learning_goal"}


def _default():
    return {"user": {"name": "", "learning_goal": ""}, "facts": [], "conversation": []}


def _validate(data):
    if not isinstance(data, dict) or not isinstance(data.get("user"), dict):
        raise ValueError("Memory 结构无效。")
    if not all(key in data["user"] for key in ALLOWED_KEYS):
        raise ValueError("Memory 缺少必要字段。")
    if not isinstance(data.get("facts"), list) or not isinstance(data.get("conversation"), list):
        raise ValueError("Memory 列表字段无效。")


def load_memory():
    if not MEMORY_PATH.exists():
        return _default()
    try:
        data = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError("memory.json 不是有效 JSON。") from error
    except OSError as error:
        raise OSError(f"读取 Memory 失败：{error}") from error
    _validate(data)
    return data


def save_memory(data):
    _validate(data)
    try:
        MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
        MEMORY_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    except OSError as error:
        raise OSError(f"保存 Memory 失败：{error}") from error


def get_memory():
    return load_memory()


def update_memory(key, value):
    if key not in ALLOWED_KEYS:
        raise ValueError("只允许更新 name 或 learning_goal。")
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Memory 内容不能为空。")
    data = load_memory()
    data["user"][key] = value.strip()
    data["facts"] = [item for item in data["facts"] if item.get("key") != key]
    data["facts"].append({"key": key, "value": value.strip()})
    save_memory(data)
    return data["user"]


def add_conversation(role, content):
    if role not in {"user", "assistant"} or not isinstance(content, str) or not content.strip():
        raise ValueError("对话记录无效。")
    data = load_memory()
    data["conversation"].append({"role": role, "content": content})
    data["conversation"] = data["conversation"][-MAX_HISTORY:]
    save_memory(data)


def get_recent_conversation():
    return load_memory()["conversation"][-MAX_HISTORY:]


def memory_context():
    user = load_memory()["user"]
    parts = []
    if user["name"]:
        parts.append(f"用户姓名：{user['name']}")
    if user["learning_goal"]:
        parts.append(f"学习目标：{user['learning_goal']}")
    return "；".join(parts) if parts else "暂无已保存用户信息。"
