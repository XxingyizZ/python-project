# 函数综合使用
# 本章使用函数组合已经学习过的if、for和列表、元组、字典、集合。

# 函数与if
# def check_score(score):
#     if score >= 60:
#         return "及格"
#     return "不及格"
#
# print(check_score(85))
# print(check_score(55))

# 函数与for
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)
#
# print_numbers([1, 2, 3, 4])

# 函数与列表：计算列表中的最大值。
# def get_max_score(scores):
#     max_score = scores[0]
#
#     for score in scores:
#         if score > max_score:
#             max_score = score
#
#     return max_score
#
# scores = [78, 92, 65, 88]
# print(get_max_score(scores))

# 函数与列表：计算列表中的总和。
# def calculate_total(numbers):
#     total = 0
#
#     for number in numbers:
#         total += number
#
#     return total
#
# numbers = [1, 2, 3, 4, 5]
# print(calculate_total(numbers))

# 函数与元组：统计元组中满足条件的数据数量。
# def count_passed_scores(scores):
#     passed_count = 0
#
#     for score in scores:
#         if score >= 60:
#             passed_count += 1
#
#     return passed_count
#
# scores = (78, 92, 56, 88)
# print(count_passed_scores(scores))

# 函数与字典：读取学生成绩。
# def get_student_score(student):
#     return student["score"]
#
# student = {"name": "小明", "score": 85}
# print(get_student_score(student))

# 函数与字典：判断学生是否及格。
# def is_passed(student):
#     return student["score"] >= 60
#
# student = {"name": "小明", "score": 85}
# print(is_passed(student))

# 函数与集合：判断元素是否存在。
# def contains_student(students, name):
#     return name in students
#
# students = {"小明", "小红", "小刚"}
# print(contains_student(students, "小明"))

# 函数与集合：返回两个集合的共同元素。
# def get_common_students(class_a, class_b):
#     return class_a & class_b
#
# class_a = {"小明", "小红", "小刚"}
# class_b = {"小红", "小刚", "小丽"}
# print(get_common_students(class_a, class_b))

# 函数与多种数据容器：获取所有及格学生的姓名。
# def get_passed_students(students):
#     passed_students = []
#
#     for student in students:
#         if student["score"] >= 60:
#             passed_students.append(student["name"])
#
#     return passed_students
#
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72}
# ]
# print(get_passed_students(students))

# 综合案例：处理学生成绩。
# def print_student_results(students):
#     passed_count = 0
#
#     for student in students:
#         if student["score"] >= 60:
#             passed_count += 1
#             print(f"{student['name']}及格")
#         else:
#             print(f"{student['name']}不及格")
#
#     return passed_count
#
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72}
# ]
# passed_count = print_student_results(students)
# print(f"及格人数：{passed_count}")

# 综合案例：列表和集合配合函数完成去重。
# def remove_duplicates(numbers):
#     return set(numbers)
#
# numbers = [1, 2, 2, 3, 3, 4]
# print(remove_duplicates(numbers))

# 函数可以把重复的数据处理逻辑组织起来，方便多次调用。
