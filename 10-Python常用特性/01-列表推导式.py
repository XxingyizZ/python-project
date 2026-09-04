# 列表推导式
# 列表推导式是一种根据已有可迭代对象快速创建列表的写法。

# 先使用普通for循环创建平方数列表。
# numbers = [1, 2, 3, 4, 5]
# squares = []
# for number in numbers:
#     squares.append(number * number)
# print(squares)

# 使用列表推导式可以写成：
# squares = [number * number for number in numbers]
# print(squares)

# 基本结构：
# [表达式 for 变量 in 可迭代对象]
# 表达式用于生成新列表中的元素。

# 带条件的列表推导式，可以筛选满足条件的元素。
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = [number for number in numbers if number % 2 == 0]
# print(even_numbers)

# 列表推导式也可以同时处理和转换数据。
# names = ["小明", "小红", "小刚"]
# messages = [f"你好，{name}" for name in names]
# print(messages)

# 列表推导式可以表示嵌套循环，但表达式复杂时可读性会降低。
# result = [x * y for x in [1, 2] for y in [3, 4]]
# print(result)

# 列表推导式不是新的数据结构，而是创建列表的一种写法。
# 如果普通for循环更容易理解，就应该使用普通for循环。
