# try / except
# try中放可能发生异常的代码，except中放发生异常时的处理代码。
# 基本结构：
# try:
#     可能发生异常的代码
# except:
#     发生异常时执行的代码

# try:
#     print(10 / 0)
# except:
#     print("发生异常")
# print("程序继续执行")

# 已知异常类型时，优先捕获具体的异常。
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("除数不能为0")

# 捕获异常后，程序可以继续执行后面的代码。
# try:
#     numbers = [1, 2, 3]
#     print(numbers[10])
# except IndexError:
#     print("索引超出范围")
# print("处理结束")

# 可以使用as e保存异常对象，并查看异常信息。
# try:
#     number = int("abc")
# except ValueError as e:
#     print(e)

# Exception可以捕获比较通用的异常，但知道具体类型时不应默认使用它。
# try:
#     print(10 / 0)
# except Exception as e:
#     print(e)

# 不建议把所有正常逻辑都放进try中，异常处理应该用于处理可能发生的异常情况。
