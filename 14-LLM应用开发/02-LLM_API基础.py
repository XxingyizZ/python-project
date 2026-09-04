# LLM API基础

# LLM API的基本流程：
# Python程序 → 发送请求 → LLM服务 → 生成结果 → 返回响应

# 访问LLM API通常有两种方式：
# 1. 直接发送HTTP请求。
# 2. 使用官方Python SDK。

# SDK是对API的一层封装，可以让Python程序更方便地调用服务。
# 本章使用OpenAI官方Python SDK和Responses API作为学习示例。

# 安装官方SDK：
# python -m pip install openai

# API Key应该通过环境变量提供，不要直接写入代码。
# import os
# api_key = os.getenv("OPENAI_API_KEY")

# 官方SDK可以自动读取OPENAI_API_KEY环境变量：
# from openai import OpenAI
# client = OpenAI()

# 最小调用流程示意：
# response = client.responses.create(
#     model="gpt-5.5",
#     input="请用一句话介绍Python。"
# )
# print(response.output_text)

# 当前不使用真实API Key进行调用，也不同时学习多个厂商的SDK。
