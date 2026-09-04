# 对象之间的关系
# 一个程序中可以同时存在多个对象。

# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
# student1 = Student("小明", 90)
# student2 = Student("小红", 85)
# student3 = Student("小刚", 72)
# students = [student1, student2, student3]
#
# for student in students:
#     if student.score >= 60:
#         print(student.name)

# 对象可以放进列表中，然后使用for循环遍历。
# 也可以在遍历时访问对象属性和调用对象方法。

# 一个对象可以保存另一个对象作为属性。
# class Teacher:
#     def __init__(self, name):
#         self.name = name
#
# class Student:
#     def __init__(self, name, teacher):
#         self.name = name
#         self.teacher = teacher
#
# teacher = Teacher("张老师")
# student = Student("小明", teacher)
# print(student.name)
# print(student.teacher.name)

# 继承：子类可以继承父类已经定义的一些属性和方法。
# class Animal:
#     def speak(self):
#         print("动物发出声音")
#
# class Dog(Animal):
#     pass
#
# dog = Dog()
# dog.speak()

# 当前只建立对象之间的简单关系和基础继承认识，不展开复杂继承设计。
