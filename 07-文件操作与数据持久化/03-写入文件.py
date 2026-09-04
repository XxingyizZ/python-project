# 写入文件
# w模式用于写入文件，文件不存在时通常会创建文件。
# 如果文件已经存在，w模式会覆盖原有内容。

# write()用于写入字符串。
# file = open("test.txt", "w", encoding="utf-8")
# file.write("hello")
# file.close()

# write()不会自动添加换行符。
# file = open("test.txt", "w", encoding="utf-8")
# file.write("hello")
# file.write("world")
# file.close()
# 上面的内容会连续写成helloworld。

# 如果需要换行，需要自己写入\n。
# file = open("test.txt", "w", encoding="utf-8")
# file.write("hello\n")
# file.write("world\n")
# file.close()

# writelines()可以写入多个字符串。
# lines = ["第一行\n", "第二行\n", "第三行\n"]
# file = open("test.txt", "w", encoding="utf-8")
# file.writelines(lines)
# file.close()

# a模式用于追加写入，会保留原有内容。
# file = open("test.txt", "a", encoding="utf-8")
# file.write("新增内容\n")
# file.close()
