# LLM API异常处理

# LLM API调用可能因为以下原因失败：
# API Key无效、网络错误、请求参数错误、权限问题、限流、服务端错误或超时。

# 调用前可以先检查必要的环境变量：
# import os
#
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     print("缺少OPENAI_API_KEY")

# 使用官方SDK时，可以捕获其异常基类：
# from openai import OpenAI
# from openai import OpenAIError
#
# client = OpenAI()
#
# try:
#     response = client.responses.create(
#         model="gpt-5.5",
#         input="请介绍Python。"
#     )
#     print(response.output_text)
# except OpenAIError as e:
#     print("LLM API调用失败：", e)

# 如果还需要捕获网络层面的异常，应根据实际SDK文档选择合适的异常类型。
# 不要为了省事而在所有程序中滥用except Exception。

# API调用也应该考虑超时和重试等实际问题。
# 不同SDK版本支持的请求选项可能不同，使用前应查看当前官方文档。
# 当前只学习基础失败处理，不展开复杂重试策略。
