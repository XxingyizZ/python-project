# 函数参数
# 参数是定义函数时用于接收数据的变量。
# 通过参数，可以让同一个函数处理不同的数据。

# 一个参数
# def greet(name):
#     print(f"你好，{name}")
#
# greet("小明")
# greet("小红")

# 调用函数时传入的值会对应到函数定义中的参数。
# def print_square(number):
#     print(number * number)
#
# print_square(3)
# print_square(5)

# 多个参数
# def add(a, b):
#     print(a + b)
#
# add(10, 20)

# 多个参数按照定义时的顺序接收传入的值。
# def introduce(name, age):
#     print(f"姓名：{name}")
#     print(f"年龄：{age}")
#
# introduce("小明", 18)

# 位置参数：调用函数时，传入的值按照位置依次对应参数。
# def subtract(a, b):
#     print(a - b)
#
# subtract(10, 3)  # a接收10，b接收3

# 参数可以接收已经保存到变量中的数据。
# x = 10
# y = 20
# add(x, y)

# 函数参数也可以接收列表等数据容器。
# def print_numbers(numbers):
#     for number in numbers:
#         print(number)
#
# numbers = [1, 2, 3, 4]
# print_numbers(numbers)

# Python函数参数不需要像C语言一样声明参数类型。
# def add(a, b):
#     return a + b
