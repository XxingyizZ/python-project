# sys与程序运行环境
# sys模块提供与Python解释器和程序运行环境有关的信息和功能。
# import sys

# sys.version可以查看当前Python版本信息。
# print(sys.version)

# sys.platform可以查看当前运行平台。
# print(sys.platform)

# sys.argv可以获取程序启动时传入的命令行参数。
# print(sys.argv)
# 如果使用命令python test.py hello 123运行程序，
# sys.argv可能类似于["test.py", "hello", "123"]。

# sys.path可以查看Python寻找模块时使用的搜索路径。
# print(sys.path)

# 当前只需要理解sys提供了程序运行环境相关的信息，
# 不展开模块搜索机制和命令行参数解析工具。
