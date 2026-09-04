# JSON综合案例
# 本章综合使用JSON、文件、函数、异常处理、列表、字典、集合、for和if。

# 将学生数据保存到JSON文件。
# def save_students(students, file_path):
#     with open(file_path, "w", encoding="utf-8") as file:
#         json.dump(students, file, ensure_ascii=False)

# 从JSON文件中读取学生数据。
# def load_students(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         return json.load(file)

# 安全读取JSON文件。
# def safe_load_students(file_path):
#     try:
#         return load_students(file_path)
#     except FileNotFoundError:
#         print("学生数据文件不存在")
#         return []
#     except json.JSONDecodeError:
#         print("学生数据的JSON格式错误")
#         return []

# 使用列表和字典保存学生数据。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72}
# ]

# 主程序可以保存数据，再读取数据并进行处理。
# import json
# save_students(students, "students.json")
# loaded_students = safe_load_students("students.json")
#
# passed_count = 0
# student_names = set()
# for student in loaded_students:
#     student_names.add(student["name"])
#     if student["score"] >= 60:
#         passed_count += 1
#         print(f"{student['name']}及格")
#
# print(f"及格人数：{passed_count}")
# print(f"不重复学生数量：{len(student_names)}")

# 数据流程：Python列表和字典 → JSON序列化 → JSON文件 → 读取并反序列化 → for和if处理。
# 当前阶段不学习JSON Schema、API、数据库、自定义编码器或第三方库。
