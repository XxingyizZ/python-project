# 程序入口与__name__

# 程序入口就是程序开始执行主要逻辑的位置。
# 最简单的程序可以直接从第一行开始执行。
# print("程序开始")

# 程序越来越复杂后，通常会把主要执行逻辑放入main函数。
# def main():
#     print("程序开始")
#
# main()

# __name__是Python提供的特殊变量。
# 一个.py文件被直接运行时，__name__的值是"__main__"。
# 一个.py文件被其他模块import时，__name__通常是模块名。

# 常见的程序入口写法：
# def main():
#     print("程序开始")
#
# if __name__ == "__main__":
#     main()

# 直接运行当前文件时，会执行main()。
# 被其他模块import时，不会自动执行这部分入口代码。

# 模块和入口的关系：
# 模块负责提供功能。
# 入口负责启动程序。

# 假设utils.py中有功能代码：
# def say_hello():
#     print("你好")

# main.py可以导入并调用它：
# import utils
#
# def main():
#     utils.say_hello()
#
# if __name__ == "__main__":
#     main()

# 当前只学习基本入口写法，不学习测试框架和复杂启动方式。
