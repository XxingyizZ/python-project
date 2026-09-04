# 文件综合使用
# 本章组合使用文件、函数、列表、字典、for、if和异常处理。

# 案例1：将列表中的学生姓名写入文件，再逐行读取。
# students = ["小明", "小红", "小刚"]
#
# with open("students.txt", "w", encoding="utf-8") as file:
#     for student in students:
#         file.write(student + "\n")
#
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         print(line.strip())

# 案例2：将字典中的学生信息保存为简单文本。
# student = {"name": "小明", "age": 18, "score": 90}
#
# with open("student.txt", "w", encoding="utf-8") as file:
#     file.write(f"姓名：{student['name']}\n")
#     file.write(f"年龄：{student['age']}\n")
#     file.write(f"成绩：{student['score']}\n")

# 案例3：使用函数负责写入和读取文件。
# def save_students(students, file_path):
#     with open(file_path, "w", encoding="utf-8") as file:
#         for student in students:
#             file.write(student + "\n")
#
# def read_students(file_path):
#     students = []
#
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             students.append(line.strip())
#
#     return students
#
# students = ["小明", "小红", "小刚"]
# save_students(students, "students.txt")
# print(read_students("students.txt"))

# 案例4：安全读取文件。
# def safe_read_file(file_path):
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "文件不存在，无法读取"
#
# print(safe_read_file("students.txt"))

# 文件对象可以使用for循环逐行读取，并结合if进行简单筛选。
# with open("students.txt", "r", encoding="utf-8") as file:
#     for line in file:
#         if line.strip() == "小明":
#             print("找到小明")

# 本章示例使用的文件路径仅用于学习说明，验证时不要擅自创建或修改项目文件。
