"""文件工具Agent的简单配置。"""

import os


API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")

try:
    MAX_STEPS = int(os.getenv("AGENT_MAX_STEPS", "5"))
except ValueError:
    MAX_STEPS = 5

if MAX_STEPS < 1:
    MAX_STEPS = 1
