# 小型Python项目：学生成绩管理

# 本案例用函数、列表、字典、异常处理、模块和程序入口，
# 体验一个小型Python项目的基本组织方式。

# 项目结构示意：
# student_project/
# ├── main.py
# ├── student.py
# └── config.py

# student.py负责学生数据处理：
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92}
# ]
#
# def add_student(students, name, score):
#     students.append({"name": name, "score": score})
#
# def get_student_score(student):
#     return student["score"]

# config.py负责简单配置：
# import os
#
# PROGRAM_NAME = os.getenv("PROGRAM_NAME", "学生成绩管理")

# main.py负责程序入口和调用其他模块：
# import student
# import config
#
# def main():
#     students = [
#         {"name": "小明", "score": 85},
#         {"name": "小红", "score": 58}
#     ]
#
#     student.add_student(students, "小刚", 72)
#     print(config.PROGRAM_NAME)
#
#     for item in students:
#         try:
#             if item["score"] >= 60:
#                 print(f"{item['name']}及格")
#             else:
#                 print(f"{item['name']}不及格")
#         except KeyError:
#             print("学生数据缺少必要字段")
#
# if __name__ == "__main__":
#     main()

# 这个项目没有数据库、Web框架、第三方库和复杂类体系。
# 重点是理解：
# 多个.py文件 → import → 函数组织功能 → main.py作为入口 → 配置从环境读取

# 实际项目中还可以配合虚拟环境、requirements.txt和.gitignore管理项目。
# 当前阶段先掌握项目工程的基本骨架，后续再按需要学习更复杂的工程工具。
