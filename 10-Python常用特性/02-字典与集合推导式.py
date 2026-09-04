# 字典与集合推导式
# 推导式也可以用于创建字典和集合。

# 字典推导式的基本结构：
# {键表达式: 值表达式 for 变量 in 可迭代对象}
# squares = {number: number * number for number in range(5)}
# print(squares)

# 字典推导式可以结合items()和if筛选数据。
# scores = {
#     "小明": 85,
#     "小红": 58,
#     "小刚": 72
# }
# passed = {
#     name: score
#     for name, score in scores.items()
#     if score >= 60
# }
# print(passed)

# 集合推导式生成的是set，重复元素不会被保留。
# numbers = [1, 2, 2, 3, 3, 4]
# unique_squares = {number * number for number in numbers}
# print(unique_squares)

# 列表推导式、字典推导式和集合推导式的区别在于结果容器不同。
# []生成列表，{}中使用键值对生成字典，{}中只使用表达式生成集合。
# 推导式应该保持简单，复杂逻辑可以改写成普通for循环。
