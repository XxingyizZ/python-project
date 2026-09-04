# JSON与异常处理
# 读取JSON文件时，可能发生文件不存在或JSON格式错误等异常。
# 文件操作异常和JSON解析异常是不同类型的问题。

# 文件不存在时会产生FileNotFoundError。
# import json
# try:
#     with open("not_found.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
# except FileNotFoundError:
#     print("JSON文件不存在")

# JSON内容格式错误时，json.load()或json.loads()可能产生JSONDecodeError。
# import json
# json_text = '{"name": "小明"'
# try:
#     data = json.loads(json_text)
# except json.JSONDecodeError:
#     print("JSON格式错误")

# 可以同时处理文件不存在和JSON格式错误。
# import json
# try:
#     with open("student.json", "r", encoding="utf-8") as file:
#         student = json.load(file)
# except FileNotFoundError:
#     print("文件不存在")
# except json.JSONDecodeError:
#     print("JSON格式错误")

# with负责文件资源管理，try和except负责处理异常。
