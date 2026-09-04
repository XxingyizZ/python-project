# Python常用特性综合使用
# 本章组合使用推导式、enumerate()、zip()、sorted()和lambda。

# 原始学生数据是列表中保存多个字典。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72},
#     {"name": "小李", "score": 92}
# ]

# 使用列表推导式获取所有学生姓名。
# names = [student["name"] for student in students]
# print(names)

# 使用字典推导式生成姓名到成绩的对应关系。
# score_map = {
#     student["name"]: student["score"]
#     for student in students
# }
# print(score_map)

# 使用集合推导式获取不重复成绩。
# unique_scores = {student["score"] for student in students}
# print(unique_scores)

# 使用enumerate()输出学生编号。
# for index, student in enumerate(students, start=1):
#     print(index, student["name"])

# 使用zip()配对姓名和成绩。
# scores = [student["score"] for student in students]
# for name, score in zip(names, scores):
#     print(name, score)

# 使用for和if筛选及格学生。
# passed_students = [
#     student["name"]
#     for student in students
#     if student["score"] >= 60
# ]
# print(passed_students)

# 使用sorted()和lambda按照成绩从高到低排序。
# sorted_students = sorted(
#     students,
#     key=lambda student: student["score"],
#     reverse=True
# )
# for student in sorted_students:
#     print(student["name"], student["score"])

# 如果推导式或lambda使代码难以阅读，可以使用普通for循环和def函数替代。
# Python常用特性是为了提高表达能力，不是为了让代码越短越好。
