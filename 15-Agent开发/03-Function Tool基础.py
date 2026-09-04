# Function Tool基础

# 先回顾一个普通Python函数：
# def add(a, b):
#     return a + b

# 需要把函数描述成模型可以理解的工具。
# from openai import OpenAI
#
# client = OpenAI()
# tools = [
#     {
#         "type": "function",
#         "name": "add",
#         "description": "计算两个数字的和。",
#         "parameters": {
#             "type": "object",
#             "properties": {
#                 "a": {"type": "number", "description": "第一个数字"},
#                 "b": {"type": "number", "description": "第二个数字"}
#             },
#             "required": ["a", "b"]
#         }
#     }
# ]

# name是工具名称，description说明工具用途。
# parameters使用基础JSON Schema描述参数类型和必填参数。

# 提供工具并请求模型：
# response = client.responses.create(
#     model="gpt-5.6",
#     tools=tools,
#     input="请计算10加20。"
# )

# 模型只会提出调用请求，Python程序仍然负责真正执行add函数。
# Python函数 → Tool描述 → LLM请求 → Python执行函数

# 当前只学习简单function tool，不学习custom tool、任意代码执行和大型框架。
