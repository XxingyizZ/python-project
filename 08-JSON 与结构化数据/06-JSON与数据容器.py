# JSON与数据容器
# JSON中的object和array与Python中的dict和list在结构上比较相似。
# import json

# Python字典可以转换成JSON字符串。
# import json
# student = {"name": "小明", "score": 90}
# json_text = json.dumps(student, ensure_ascii=False)
# print(json_text)

# 列表中可以保存多个字典，这种结构很适合表示多条结构化数据。
# students = [
#     {"name": "小明", "score": 90},
#     {"name": "小红", "score": 85}
# ]
# json_text = json.dumps(students, ensure_ascii=False)
# print(json_text)

# 字典和列表可以组合成嵌套数据。
# students = {
#     "class_name": "Python班",
#     "students": [
#         {"name": "小明", "score": 90},
#         {"name": "小红", "score": 85}
#     ]
# }
# json_text = json.dumps(students, ensure_ascii=False)
# print(json_text)

# 反序列化后，可以继续使用字典、列表、for和if处理数据。
# data = json.loads(json_text)
# for student in data["students"]:
#     if student["score"] >= 60:
#         print(student["name"])

# JSON负责表示和交换数据，Python负责读取和处理数据。
