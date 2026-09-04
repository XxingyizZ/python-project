# 模块与包综合使用
# 本章使用已经学习过的函数、参数、return、列表、字典、集合和if、for。

# 假设student_tools.py中定义了下面的函数：
# def get_average_score(scores):
#     total = 0
#
#     for score in scores:
#         total += score
#
#     return total / len(scores)
#
# def get_passed_students(students):
#     passed_students = []
#
#     for student in students:
#         if student["score"] >= 60:
#             passed_students.append(student["name"])
#
#     return passed_students

# main.py导入student_tools模块后，可以调用其中的函数。
# import student_tools
#
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72}
# ]
# scores = [85, 58, 72]
#
# print(student_tools.get_average_score(scores))
# print(student_tools.get_passed_students(students))

# 数据由列表和字典保存，函数负责处理数据，模块负责组织函数。
# 数据 → 函数 → 模块 → 主程序

# 也可以把去重函数放在data_tools.py中。
# def remove_duplicates(numbers):
#     return set(numbers)
#
# 主程序中导入并使用：
# import data_tools
#
# numbers = [1, 2, 2, 3, 3, 4]
# print(data_tools.remove_duplicates(numbers))

# 如果相关模块放在tools包中，可以从包中导入模块。
# from tools import student_tools
# print(student_tools.get_passed_students(students))

# 函数、模块和包的关系：
# 函数组织一段功能代码；模块组织多个函数和变量；包组织多个相关模块。

# 当前阶段只学习基本的import、from ... import ...、自定义模块和包。
# sys.path、动态导入、循环导入、包发布等内容留到后续学习。
