# __init__与self
# __init__方法会在创建对象时被调用，常用于初始化对象属性。

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# student = Student("小明", 90)
# print(student.name)
# print(student.score)

# 创建Student对象时，传入的参数会交给__init__，用于初始化属性。
# Student(...)
#     ↓
# 创建对象
#     ↓
# 调用__init__
#     ↓
# 初始化对象属性

# self表示当前对象本身。
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# student1 = Student("小明", 90)
# student2 = Student("小红", 85)
# print(student1.name)
# print(student2.name)

# student1和student2是不同对象，各自保存自己的name和score。

# 方法中可以通过self访问当前对象的属性。
# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def introduce(self):
#         print(f"我叫{self.name}")
#
# student = Student("小明")
# student.introduce()

# 调用student.introduce()时，可以把当前对象理解为self对应的对象。

# 对象的属性可以表示对象当前的状态。
# student = Student("小明", 90)
# student.score = 95
# print(student.score)
