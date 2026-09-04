# 数据持久化综合案例
# 持久化就是让程序中的数据在程序结束后仍然能够保存。
# 数据 → 文件 → 程序结束 → 再次读取 → 继续使用

# 使用列表和字典保存学生数据。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 58},
#     {"name": "小刚", "score": 72}
# ]

# 将学生数据保存为简单的文本格式。
# def save_students(students, file_path):
#     with open(file_path, "w", encoding="utf-8") as file:
#         for student in students:
#             file.write(f"{student['name']},{student['score']}\n")

# 读取文件中的学生数据，并重新组织为列表和字典。
# def read_students(file_path):
#     students = []
#
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             name, score = line.strip().split(",")
#             students.append({"name": name, "score": int(score)})
#
#     return students

# 使用try和except处理文件不存在的情况。
# def safe_read_students(file_path):
#     try:
#         return read_students(file_path)
#     except FileNotFoundError:
#         print("数据文件不存在")
#         return []

# 对重新读取的数据进行简单处理。
# loaded_students = safe_read_students("students.txt")
# passed_count = 0
#
# for student in loaded_students:
#     if student["score"] >= 60:
#         passed_count += 1
#         print(f"{student['name']}及格")
#
# print(f"及格人数：{passed_count}")

# 集合可以用于统计不重复的学生姓名。
# student_names = set()
# for student in loaded_students:
#     student_names.add(student["name"])
# print(f"不重复学生数量：{len(student_names)}")

# 当前案例重点是理解数据从内存保存到文件，再从文件读取回来。
# 不在本章提前学习JSON、CSV、数据库或复杂文件格式。

# Python中通常使用with自动管理文件关闭，C语言中通常需要显式调用fclose()。
# 两者都有文件操作，但Python的import、with和文件对象机制不能简单等同于C语言的写法。
