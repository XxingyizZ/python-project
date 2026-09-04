# 消息与Prompt

# Prompt是给模型的输入指令或内容。
# 例如：
# 请把下面这段文字总结成三句话。

# 用户输入可以保存在变量中：
# user_text = "Python可以帮助我们快速编写程序。"
# prompt = f"请总结下面的内容：{user_text}"

# 使用Responses API时，可以使用input传递文本：
# from openai import OpenAI
# client = OpenAI()
# response = client.responses.create(
#     model="gpt-5.5",
#     input=prompt
# )
# print(response.output_text)

# 也可以使用消息列表表达角色和内容：
# response = client.responses.create(
#     model="gpt-5.5",
#     instructions="你是一个简洁的学习助手。",
#     input=[
#         {"role": "user", "content": "请解释变量是什么。"}
#     ]
# )

# instructions可以提供更高层次的行为指引。
# user消息表示本次用户输入。
# 多轮对话中的assistant消息可以表示模型之前的回答。

# 基础Prompt原则：
# 1. 目标明确。
# 2. 提供必要的上下文。
# 3. 规定需要的输出形式。
# 4. 避免模糊要求。

# 示例：
# 请把下面内容总结成3条，每条不超过20个字。

# 当前不学习CoT、ReAct、Self-consistency等高级Prompt方法。
