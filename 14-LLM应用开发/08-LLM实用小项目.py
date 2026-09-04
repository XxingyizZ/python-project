# LLM实用小项目：AI文本分析助手

# 项目目标：
# 用户输入一段文本 → Python调用LLM → 返回结构化分析结果 → Python解析并输出。

# 可以让模型返回类似下面的结构：
# {
#     "summary": "文本的简短总结",
#     "sentiment": "positive",
#     "keywords": ["Python", "学习"]
# }

# import json
# import os
# from openai import OpenAI
#
# def call_llm(text):
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
#     prompt = (
#         "请分析下面的文本，只输出JSON，包含summary、sentiment和keywords字段。"
#         f"\n文本：{text}"
#     )
#     response = client.responses.create(
#         model="gpt-5.5",
#         input=prompt
#     )
#     return response.output_text
#
# def analyze_text(text):
#     result_text = call_llm(text)
#     return json.loads(result_text)
#
# def main():
#     if not os.getenv("OPENAI_API_KEY"):
#         print("缺少OPENAI_API_KEY，无法调用LLM。")
#         return
#
#     text = input("请输入要分析的文本：")
#
#     try:
#         result = analyze_text(text)
#         print(f"总结：{result['summary']}")
#         print(f"情感：{result['sentiment']}")
#         print(f"关键词：{result['keywords']}")
#     except json.JSONDecodeError:
#         print("模型返回的内容不是有效JSON。")
#     except Exception as e:
#         print("调用LLM失败：", e)
#
# if __name__ == "__main__":
#     main()

# 这个项目综合使用了：
# 函数、模块、程序入口、环境变量、API、JSON、字典和异常处理。

# input()和真实LLM调用需要用户输入、SDK和API Key，因此只进行静态检查。
# 当前不学习Tool Calling、RAG、Memory、多Agent、LangChain或LangGraph。
