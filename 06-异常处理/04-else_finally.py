# try / except / else / finally
# else中的代码会在try没有发生异常时执行。
# finally中的代码通常都会执行，无论try中是否发生异常。

# try:
#     number = int("123")
# except ValueError:
#     print("转换失败")
# else:
#     print("转换成功")

# 异常处理中的else和条件判断中的else作用不同。
# 这里的else表示try代码没有发生异常时执行。

# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("发生异常")
# finally:
#     print("处理结束")

# try没有发生异常时，else和finally都可以执行。
# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("除数不能为0")
# else:
#     print(result)
# finally:
#     print("程序处理结束")

# 当前阶段只需要理解else和finally的基本执行条件，不展开资源管理等内容。
