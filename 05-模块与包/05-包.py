# 包
# 包可以用来组织多个相关模块。
# 一个包中可以保存多个.py模块文件。

# 可以把项目组织成下面的结构：
# 项目目录/
#     main.py
#     tools/
#         __init__.py
#         math_tools.py
#         student_tools.py

# tools是一个包，math_tools.py和student_tools.py是包中的模块。
# __init__.py可以帮助Python识别和组织这个包。
# 当前只需要建立包和模块的基本认识，不展开包的导入机制。

# 可以导入包中的模块。
# import tools.math_tools
# print(tools.math_tools.add(10, 20))

# 也可以使用from ... import ...导入包中的模块。
# from tools import math_tools
# print(math_tools.add(10, 20))

# 还可以从包中的模块导入指定函数。
# from tools.math_tools import add
# print(add(10, 20))

# 包用于组织多个相关模块，模块用于组织函数和变量。
# 函数 → 模块 → 包，是逐步组织代码的关系。
