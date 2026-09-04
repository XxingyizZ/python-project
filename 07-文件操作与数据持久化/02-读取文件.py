# 读取文件
# 可以使用open()打开文件，再使用文件对象读取内容。

# read()读取文件的全部内容，返回一个字符串。
# file = open("test.txt", "r", encoding="utf-8")
# content = file.read()
# print(content)
# file.close()

# readline()读取文件中的一行。
# file = open("test.txt", "r", encoding="utf-8")
# line = file.readline()
# print(line)
# file.close()

# readlines()读取多行，返回一个列表，列表中的每个元素通常对应一行内容。
# file = open("test.txt", "r", encoding="utf-8")
# lines = file.readlines()
# print(lines)
# file.close()

# read()、readline()和readlines()的区别：
# read()读取全部内容，结果是字符串。
# readline()读取一行，结果是字符串。
# readlines()读取多行，结果是列表。

# 文件对象可以直接使用for循环逐行读取。
# file = open("test.txt", "r", encoding="utf-8")
# for line in file:
#     print(line)
# file.close()
