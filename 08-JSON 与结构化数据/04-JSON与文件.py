# JSON与文件
# json.dump()可以把Python对象直接写入JSON文件。
# json.load()可以从JSON文件中读取数据并转换成Python对象。

# import json
# student = {
#     "name": "小明",
#     "age": 18,
#     "score": 90
# }
#
# with open("student.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False)

# 使用json.load()读取JSON文件。
# import json
# with open("student.json", "r", encoding="utf-8") as file:
#     student = json.load(file)
# print(student)

# dumps和loads处理JSON字符串，dump和load可以直接配合文件对象使用。
# dumps：Python对象 → JSON字符串
# loads：JSON字符串 → Python对象
# dump：Python对象 → JSON文件
# load：JSON文件 → Python对象

# ensure_ascii=False可以让JSON文件中的中文直接显示为中文。
# with open("student.json", "w", encoding="utf-8") as file:
#     json.dump(student, file, ensure_ascii=False)

# with负责管理文件资源，open负责打开文件，json.dump或json.load负责转换数据。
