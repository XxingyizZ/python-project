# LLM应用综合使用

# 案例一：文本总结
# import os
# from openai import OpenAI
#
# api_key = os.getenv("OPENAI_API_KEY")
# if api_key:
#     client = OpenAI(api_key=api_key)
#     text = "Python是一种适合快速开发的编程语言。"
#     prompt = f"请用一句话总结下面的内容：{text}"
#     response = client.responses.create(
#         model="gpt-5.5",
#         input=prompt
#     )
#     print(response.output_text)

# 案例二：文本分类
# feedback = "课程内容清晰，我学会了列表和字典。"
# prompt = f"请判断这段反馈是positive、neutral还是negative，只输出类别：{feedback}"
# response = client.responses.create(
#     model="gpt-5.5",
#     input=prompt
# )
# print(response.output_text)

# 案例三：结构化信息提取
# import json
#
# text = "小明今年18岁，住在北京。"
# prompt = f"请从下面内容提取name、age、city，并只输出JSON：{text}"
# response = client.responses.create(
#     model="gpt-5.5",
#     input=prompt
# )
#
# try:
#     result = json.loads(response.output_text)
#     print(result["name"])
#     print(result["age"])
#     print(result["city"])
# except json.JSONDecodeError:
#     print("模型输出不是有效JSON")

# LLM应用的基本流程：
# 用户输入 → 构造Prompt → 调用LLM → 获取文本 → 解析或处理 → 输出结果
