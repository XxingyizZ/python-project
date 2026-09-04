# 常见异常
# 不同的问题可能产生不同类型的异常。

# ZeroDivisionError：除数不能为0。
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("除数不能为0")

# IndexError：列表索引超出有效范围。
# numbers = [1, 2, 3]
# try:
#     print(numbers[10])
# except IndexError:
#     print("索引超出范围")

# KeyError：字典中不存在指定的key。
# student = {"name": "小明"}
# try:
#     print(student["score"])
# except KeyError:
#     print("字典中没有这个key")

# TypeError：数据类型不支持当前操作。
# try:
#     print(10 + "20")
# except TypeError:
#     print("数据类型不匹配")

# ValueError：数据类型正确，但数据内容不符合要求。
# try:
#     number = int("abc")
# except ValueError:
#     print("数据内容不能转换为整数")

# 多个except可以分别处理不同类型的异常。
# try:
#     number = int("10")
#     result = 10 / number
#     print(result)
# except ValueError:
#     print("请输入有效数字")
# except ZeroDivisionError:
#     print("除数不能为0")
