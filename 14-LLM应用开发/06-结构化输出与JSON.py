# 结构化输出与JSON

# 自然语言适合人阅读，但程序通常更适合处理结构化数据。
# 例如：
# 姓名：小明
# 年龄：18
# 城市：北京

# 如果模型返回JSON对象，程序更容易继续处理：
# {
#     "name": "小明",
#     "age": 18,
#     "city": "北京"
# }

# 可以在Prompt中明确要求只输出JSON：
# prompt = "请把下面信息整理成JSON对象，只输出JSON。小明18岁，住在北京。"

# 得到文本后，可以使用json.loads()解析：
# import json
#
# text = '{"name": "小明", "age": 18, "city": "北京"}'
# try:
#     data = json.loads(text)
#     print(data["name"])
# except json.JSONDecodeError:
#     print("模型返回的内容不是有效JSON")

# 当前官方Responses API也提供结构化输出能力，可以帮助模型按指定格式返回结果。
# 这里只做基础认识，不展开复杂JSON Schema。

# 模型输出不是永远可靠的。
# 即使要求输出JSON，也应该在Python程序中解析并检查结果。
