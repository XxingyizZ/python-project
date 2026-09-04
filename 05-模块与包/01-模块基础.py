# 模块基础
# 一个.py文件可以作为一个模块使用。
# 模块可以把相关的函数和变量组织到一个文件中，方便管理和复用。

# 第四章学习了使用函数组织一段功能代码。
# 模块可以进一步把多个函数和变量组织到不同的文件中。
# 一个.py文件可以包含函数、变量等名称。

# 例如，下面的内容可以放在math_tools.py中。
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b

# 另一个.py文件可以导入这个模块并使用其中的函数。
# import math_tools
# print(math_tools.add(10, 20))
# print(math_tools.multiply(3, 4))

# 模块中的变量也可以被使用。
# 例如，math_tools.py中还可以有：
# PI = 3.14
#
# 导入后可以通过模块名访问变量：
# import math_tools
# print(math_tools.PI)

# 模块可以帮助我们把代码拆分到不同文件中，而不是把所有代码写在一个文件里。
# Python一个.py文件就可以成为模块，不需要像C语言一样单独编写头文件声明函数。
