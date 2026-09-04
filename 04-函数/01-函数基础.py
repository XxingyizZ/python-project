# 函数基础
# 函数可以把一段具有特定功能的代码组织起来，并且可以重复调用。
# 函数可以接收数据，也可以返回处理后的结果。

# 定义函数
# 使用def关键字定义函数，函数体需要缩进。
# def 函数名():
#     函数体

# 定义函数和执行函数不是一回事。
# def greet():
#     print("你好")

# 调用函数时，函数体中的代码才会执行。
# greet()

# 函数可以被调用多次。
# def greet():
#     print("你好")
#
# greet()
# greet()

# 函数可以把重复的代码组织起来。
# def print_welcome():
#     print("欢迎学习Python")
#
# print_welcome()
# print_welcome()

# 函数的名称应该能够表达函数的功能，多个单词可以使用下划线连接。
# def print_student_name():
#     print("小明")
#
# print_student_name()

# Python使用缩进表示函数体，不需要像C语言一样使用大括号。
# Python函数也不需要像C语言一样提前声明返回值类型。

# 函数也可以保存到变量中，或者放进字典中统一管理。
# 这也是后面把Python函数注册成Tool时的重要基础。
# def hello():
#     print("hello")
#
# func = hello
# func()
#
# tools = {"hello": hello}
# tools["hello"]()

# 这里先理解“函数可以作为对象使用”，暂时不学习复杂的框架或设计模式。
