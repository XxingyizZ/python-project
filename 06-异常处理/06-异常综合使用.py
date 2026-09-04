# 异常综合使用
# 本章使用已经学习过的函数、列表、字典、集合、for和if。

# 函数内部可以使用try / except处理异常。
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return None
#
# print(divide(10, 2))
# print(divide(10, 0))

# 安全转换数字。
# def convert_number(value):
#     try:
#         return int(value)
#     except ValueError:
#         return None
#
# print(convert_number("123"))
# print(convert_number("abc"))

# 列表和异常处理：捕获列表索引超出范围的问题。
# def get_number(numbers, index):
#     try:
#         return numbers[index]
#     except IndexError:
#         return None
#
# numbers = [10, 20, 30]
# print(get_number(numbers, 1))
# print(get_number(numbers, 10))

# 字典和异常处理：处理可能不存在的key。
# def get_student_score(student):
#     try:
#         return student["score"]
#     except KeyError:
#         return None
#
# student = {"name": "小明"}
# print(get_student_score(student))

# 学生数据处理：如果某条数据缺少score，可以捕获KeyError并继续处理其他数据。
# def print_scores(students):
#     for student in students:
#         try:
#             print(f"{student['name']}：{student['score']}")
#         except KeyError:
#             print(f"{student['name']}没有成绩数据")
#
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红"},
#     {"name": "小刚", "score": 72}
# ]
# print_scores(students)

# 集合和异常处理：集合成员判断通常使用in，不需要为了正常判断而使用异常。
# students = {"小明", "小红", "小刚"}
# if "小明" in students:
#     print("小明在集合中")

# 综合案例：统计学生成绩，并处理缺少成绩的数据。
# def count_passed_students(students):
#     passed_count = 0
#
#     for student in students:
#         try:
#             if student["score"] >= 60:
#                 passed_count += 1
#         except KeyError:
#             print(f"{student['name']}缺少成绩数据")
#
#     return passed_count
#
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红"},
#     {"name": "小刚", "score": 72}
# ]
# print(f"及格人数：{count_passed_students(students)}")

# 异常处理是为了处理可能发生的异常情况，不应代替正常的if条件判断。
# C语言中常通过返回值或错误码处理错误，Python可以使用try / except捕获异常。
# 这两种方式用途有相似之处，但机制并不相同。

# 当前阶段不学习自定义异常类、异常继承体系、with、traceback和高级异常设计。
