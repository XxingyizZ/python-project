# 变量作用域
# 变量作用域表示变量可以被使用的范围。

# 函数内部定义的变量通常是局部变量，只能在函数内部使用。
# def test():
#     number = 10
#     print(number)
#
# test()

# 函数外部不能直接使用函数内部的局部变量。
# def test():
#     number = 10
#
# test()
# print(number)  # 会产生NameError

# 每次调用函数时，函数内部的局部变量在函数内部使用。
# def add(a, b):
#     result = a + b
#     return result
#
# print(add(10, 20))

# 函数可以读取函数外部已经存在的变量。
# message = "你好"
#
# def greet():
#     print(message)
#
# greet()

# 如果函数内部和外部存在同名变量，函数内部的变量会在函数内部使用。
# number = 100
#
# def test():
#     number = 10
#     print(number)
#
# test()
# print(number)

# 当前阶段只需要理解函数内部变量和外部变量的基本区别。
# global、nonlocal以及更复杂的作用域规则留到后续学习。
