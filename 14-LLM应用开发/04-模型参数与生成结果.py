# 模型参数与生成结果

# 调用模型时，除了输入内容，还可以指定模型和一些生成参数。

# model用于指定使用哪个模型。
# 不同模型的能力、速度、价格和上下文能力可能不同。

# 使用OpenAI Responses API的基础示例：
# from openai import OpenAI
# client = OpenAI()
# response = client.responses.create(
#     model="gpt-5.5",
#     input="请用两句话介绍列表。"
# )
# print(response.output_text)

# temperature可以影响生成结果的随机程度。
# 较低的值通常更集中，较高的值通常可能更有变化。
# 不同模型和任务的实际效果需要通过测试观察。
# response = client.responses.create(
#     model="gpt-5.5",
#     input="写一句学习Python的建议。",
#     temperature=0.2
# )

# max_output_tokens可以限制模型最多生成的Token数量。
# response = client.responses.create(
#     model="gpt-5.5",
#     input="介绍Python。",
#     max_output_tokens=100
# )

# response.output_text是SDK提供的便捷方式，用于读取模型生成的文本。
# 不要默认只访问output列表中的第一个元素来获取文本。

# 基本关系：输入 + 模型 + 生成参数 → 模型 → 输出。
# 当前不学习流式输出、工具调用和多模型评测。
