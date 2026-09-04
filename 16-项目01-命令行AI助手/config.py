"""命令行AI助手的配置。"""

import os


API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6")


def get_api_key():
    """读取API Key；缺失时返回None，由调用方给出提示。"""
    return API_KEY
