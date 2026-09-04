# 面向对象综合使用
# 本章组合使用类、对象、属性、方法、self、__init__、列表、for和if。

# 定义Student类。
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def is_passed(self):
#         return self.score >= 60

# 创建多个Student对象，并把对象保存到列表中。
# students = [
#     Student("小明", 85),
#     Student("小红", 58),
#     Student("小刚", 72)
# ]

# 遍历对象列表，访问对象属性并调用对象方法。
# for student in students:
#     if student.is_passed():
#         print(f"{student.name}及格")
#     else:
#         print(f"{student.name}不及格")

# 统计及格人数。
# passed_count = 0
# for student in students:
#     if student.is_passed():
#         passed_count += 1
# print(f"及格人数：{passed_count}")

# 对象的属性可以先转换成字典，再用于JSON等结构化数据处理。
# student_data = {
#     "name": students[0].name,
#     "score": students[0].score
# }
# print(student_data)

# 可以使用异常处理检查输入数据，但异常处理不是面向对象的核心。
# try:
#     score = int("85")
# except ValueError:
#     print("成绩输入错误")

# 看到下面的代码时，可以这样理解：
# class Agent:
#     def __init__(self, name):
#         self.name = name
#
#     def run(self):
#         print(self.name)
#
# agent = Agent("助手")
# agent.run()
# Agent是类，agent是对象，self.name是对象属性，run()是对象方法。

# 当前阶段不学习property、dataclass、多继承、super()深入机制、魔术方法和设计模式。
