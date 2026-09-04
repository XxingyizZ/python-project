# sorted()与lambda基础
# sorted()可以对数据进行排序，并返回一个新的排序结果。

# numbers = [5, 2, 8, 1]
# result = sorted(numbers)
# print(result)
# print(numbers)  # 原列表没有被sorted()修改

# reverse=True可以让排序结果按降序排列。
# numbers = [5, 2, 8, 1]
# print(sorted(numbers, reverse=True))

# 列表的sort()会直接修改原列表，sorted()会返回新的结果。
# numbers = [5, 2, 8, 1]
# numbers.sort()
# print(numbers)

# key参数可以告诉sorted()按照什么数据进行排序。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 72}
# ]
# result = sorted(students, key=lambda student: student["score"])
# print(result)

# lambda的基本形式：lambda 参数: 表达式
# add = lambda a, b: a + b
# print(add(10, 20))

# lambda可以完成简单、短小的函数。
# def get_score(student):
#     return student["score"]
#
# print(sorted(students, key=get_score))
# print(sorted(students, key=lambda student: student["score"]))

# lambda适合简单的一次性逻辑，不是所有场景都比def更好。
