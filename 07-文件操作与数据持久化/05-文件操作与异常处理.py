# 文件操作与异常处理
# 文件操作可能发生异常，例如读取不存在的文件。
# with负责文件资源管理，try和except负责异常处理，它们解决的是不同的问题。

# 读取不存在的文件时，可能产生FileNotFoundError。
# with open("not_found.txt", "r", encoding="utf-8") as file:
#     print(file.read())

# 可以使用try和except处理文件不存在的情况。
# try:
#     with open("not_found.txt", "r", encoding="utf-8") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("文件不存在")

# 使用函数封装安全读取文件的逻辑。
# def read_file(file_path):
#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             return file.read()
#     except FileNotFoundError:
#         return "文件不存在"
#
# print(read_file("test.txt"))

# 相对路径是相对于程序当前运行环境的路径。
# open("data.txt", "r", encoding="utf-8")

# 绝对路径从文件系统的根位置或盘符开始描述文件位置。
# 当前阶段只需要区分相对路径和绝对路径，不展开复杂路径规则。
# ./表示当前目录，../表示上一级目录。

# 中文文本通常需要注意编码，encoding="utf-8"是常见写法。
