# 可迭代对象与迭代器
# 可以被for循环逐个访问的对象，可以称为可迭代对象。
# list、tuple、dict、set和str都可以使用for循环遍历。

# numbers = [10, 20, 30]
# for number in numbers:
#     print(number)

# iter()可以从可迭代对象得到一个迭代器。
# numbers = [10, 20, 30]
# iterator = iter(numbers)

# next()可以从迭代器中一次获取一个元素。
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# 迭代器没有更多元素时，继续调用next()会产生StopIteration。
# try:
#     print(next(iterator))
# except StopIteration:
#     print("没有更多元素")

# 可迭代对象可以被for遍历，迭代器可以通过next()逐个取得元素。
# for循环可以帮助我们自动完成逐个取值的过程。

# 当前只学习iter()、next()和StopIteration的基础认识，不实现自定义迭代器。
