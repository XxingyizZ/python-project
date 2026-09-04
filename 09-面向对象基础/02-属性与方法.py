# 属性与方法
# 属性表示对象保存的数据，方法表示对象可以执行的行为。

# 可以给对象添加属性。
# class Student:
#     pass
#
# student = Student()
# student.name = "小明"
# student.score = 90
# print(student.name)
# print(student.score)

# 方法是定义在类中的函数，可以通过对象调用。
# class Student:
#     def study(self):
#         print("正在学习")
#
# student = Student()
# student.study()

# 属性和方法的关系：
# 属性 → 对象保存的数据
# 方法 → 对象可以执行的行为

# 方法本质上也是定义在类中的函数，但通常通过对象调用。
# def add(a, b):
#     return a + b
#
# class Student:
#     def study(self):
#         print("学习")
#
# result = add(10, 20)
# student = Student()
# student.study()
