# API返回数据处理

# API返回的JSON数据通常会被解析为Python字典或列表。
# JSON：{"name": "Tom", "score": 90}
#
# result = response.json()
# print(result["name"])
# print(result["score"])

# 如果响应中包含学生列表：
# data = {
#     "students": [
#         {"name": "Tom", "score": 90},
#         {"name": "Lucy", "score": 95}
#     ]
# }
#
# students = data["students"]
# for student in students:
#     print(student["name"])

# 也可以使用函数处理API数据：
# def get_student_names(data):
#     names = []
#
#     for student in data["students"]:
#         names.append(student["name"])
#
#     return names
#
# print(get_student_names(data))

# API数据和已经学习过的列表、字典、集合、for、if可以组合使用。
# 例如筛选成绩、统计数量或去除重复数据。
# 当前不使用pandas等第三方数据处理工具。
