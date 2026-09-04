"""读取、保存和更新JSON Memory。"""

import json
from pathlib import Path

from config import MAX_HISTORY


MEMORY_PATH = Path(__file__).resolve().parent / "data" / "memory.json"
ALLOWED_KEYS = {"name", "learning_goal"}


def _default_memory():
    return {
        "user": {"name": "", "learning_goal": ""},
        "facts": [],
        "conversation": [],
    }


def _validate_memory(memory):
    if not isinstance(memory, dict):
        raise ValueError("Memory必须是字典。")
    if not isinstance(memory.get("user"), dict):
        raise ValueError("Memory缺少user字典。")
    if not all(key in memory["user"] for key in ALLOWED_KEYS):
        raise ValueError("user字段缺少必要的Memory key。")
    if not isinstance(memory.get("facts"), list):
        raise ValueError("facts必须是列表。")
    if not isinstance(memory.get("conversation"), list):
        raise ValueError("conversation必须是列表。")


def load_memory():
    """读取Memory；文件不存在时返回初始结构。"""
    if not MEMORY_PATH.exists():
        return _default_memory()

    try:
        memory = json.loads(MEMORY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ValueError("memory.json不是有效JSON。") from e
    except OSError as e:
        raise OSError(f"读取Memory失败：{e}") from e

    _validate_memory(memory)
    return memory


def save_memory(memory):
    """验证并保存Memory。"""
    _validate_memory(memory)
    try:
        MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
        MEMORY_PATH.write_text(
            json.dumps(memory, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError as e:
        raise OSError(f"保存Memory失败：{e}") from e


def get_memory():
    """返回当前Memory。"""
    return load_memory()


def update_memory(key, value):
    """更新允许的长期记忆字段。"""
    if key not in ALLOWED_KEYS:
        raise ValueError("不允许修改这个Memory key。")
    if not isinstance(value, str):
        raise TypeError("Memory value必须是字符串。")

    memory = load_memory()
    memory["user"][key] = value
    fact = {"key": key, "value": value}
    memory["facts"] = [item for item in memory["facts"] if item.get("key") != key]
    memory["facts"].append(fact)
    save_memory(memory)
    return memory


def add_conversation(role, content):
    """保存一条对话，并只保留最近有限条记录。"""
    if role not in {"user", "assistant"}:
        raise ValueError("对话role必须是user或assistant。")
    if not isinstance(content, str) or not content:
        raise ValueError("对话content不能为空。")

    memory = load_memory()
    memory["conversation"].append({"role": role, "content": content})
    memory["conversation"] = memory["conversation"][-MAX_HISTORY:]
    save_memory(memory)
    return memory
