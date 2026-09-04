# 自定义模块
# 模块不仅可以是Python标准库，也可以是自己编写的.py文件。

# 假设当前目录中有math_tools.py文件，内容如下：
# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b

# 另一个main.py文件可以导入math_tools模块。
# import math_tools
# print(math_tools.add(10, 20))
# print(math_tools.multiply(3, 4))

# 自定义模块中也可以保存变量。
# 假设math_tools.py中还有：
# PI = 3.14
#
# import math_tools
# print(math_tools.PI)

# 通过模块名访问函数和变量，可以清楚地知道名称来自哪个模块。
# 模块名.函数名
# 模块名.变量名

# 自定义模块的作用是把相关功能放到一个单独的.py文件中，供其他文件使用。
# 当前只学习简单、正常的模块导入，不讨论循环导入和模块加载细节。
