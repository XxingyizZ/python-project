# with语句
# with可以帮助我们管理文件资源。
# 离开with代码块后，文件会被自动关闭。

# with open("test.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# 使用with后，不需要手动调用file.close()。
# 文件操作的基本流程是：open → 使用文件 → 离开with → 文件自动关闭。

# 使用with写入文件。
# with open("test.txt", "w", encoding="utf-8") as file:
#     file.write("你好，Python\n")

# 使用with追加内容。
# with open("test.txt", "a", encoding="utf-8") as file:
#     file.write("继续学习文件操作\n")

# 实际开发中，文件操作通常优先使用with语句。
# with负责资源管理，不负责处理文件内容本身的异常，异常处理会使用try和except。
