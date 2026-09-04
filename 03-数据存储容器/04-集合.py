# 集合是数据容器的一类，可以存储多个不重复的元素
# 集合适合用于判断元素是否存在，以及处理集合之间的关系。
# 集合中的元素不能重复，集合是可变对象，可以进行添加和删除。
# 集合不支持像列表一样的索引位置，不能依赖集合元素的遍历顺序。

# 集合的创建
# numbers = {1, 2, 3}
# print(numbers)

# 集合中的重复元素不会被保留。
# numbers = {1, 2, 2, 3, 3}
# print(numbers)  # {1, 2, 3}

# 空集合需要使用set()创建。
# empty_set = set()
# print(empty_set)

# 注意，{}表示空字典，不是空集合。
# empty_dict = {}
# print(empty_dict)

# 集合元素
# 当前主要使用数字和字符串作为集合元素。
# 集合中的元素需要满足Python对集合元素的基本要求，更复杂的规则以后再学习。
# names = {"小明", "小红", "小刚"}
# numbers = {1, 2, 3}
# print(names)
# print(numbers)

# 集合成员判断
# 集合特别适合判断某个元素是否存在。
# numbers = {1, 2, 3}
# print(2 in numbers)      # True
# print(5 in numbers)      # False
# print(5 not in numbers)  # True

# 列表同样支持in成员判断，但集合常用于表达“不重复的成员集合”。
# print(2 in [1, 2, 3])
# print(2 in {1, 2, 3})

# 集合添加元素
# add()用于向集合中添加一个元素。
# numbers = {1, 2, 3}
# numbers.add(4)
# numbers.add(2)  # 2已经存在，不会产生重复元素
# print(numbers)

# 集合删除元素
# remove()用于删除指定元素，元素不存在时会产生KeyError。
# numbers = {1, 2, 3}
# numbers.remove(2)
# print(numbers)

# discard()也可以删除指定元素，元素不存在时不会报错。
# numbers = {1, 2, 3}
# numbers.discard(2)
# numbers.discard(5)
# print(numbers)

# 集合的pop()与列表的pop(index)不同。
# 集合没有固定索引，pop()会删除并返回一个元素，不应依赖具体删除哪一个元素。
# 当前阶段暂不展开使用pop()。

# 集合遍历
# 集合可以使用for循环遍历，但不能像列表一样使用数字索引。
# numbers = {1, 2, 3}
# for number in numbers:
#     print(number)

# numbers[0]  # 会产生TypeError，集合不支持数字索引
# 不要依赖集合遍历时元素出现的具体顺序。

# 集合基本运算
# 并集：合并两个集合中的所有元素，重复元素只保留一份。
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}
# print(set_a | set_b)
# print(set_a.union(set_b))

# 交集：取得两个集合中都存在的元素。
# print(set_a & set_b)
# print(set_a.intersection(set_b))

# 差集：取得存在于set_a但不存在于set_b的元素。
# print(set_a - set_b)
# print(set_a.difference(set_b))

# 对称差集暂不作为当前重点，后续再学习。

# 列表和集合转换
# 可以使用set()将列表转换为集合，从而去除重复元素。
# numbers = [1, 2, 2, 3, 3, 4]
# unique_numbers = set(numbers)
# print(unique_numbers)

# 也可以使用list()将集合转换为列表。
# set_data = {1, 2, 3}
# list_data = list(set_data)
# print(list_data)
# 集合不提供像列表一样的固定索引位置，转换后不要依赖元素的顺序。

# 集合与if条件判断
# numbers = {10, 15, 20, 25, 30}
# for number in numbers:
#     if number >= 20:
#         print(number)

# 综合案例：两组数据的集合关系
# class_a = {"小明", "小红", "小刚"}
# class_b = {"小红", "小刚", "小丽"}
#
# common_students = class_a & class_b
# only_in_a = class_a - class_b
# all_students = class_a | class_b
#
# print("两班都有的学生：", common_students)
# print("只在A班的学生：", only_in_a)
# print("两个班的全部学生：", all_students)

# 综合案例：集合成员判断
# students = {"小明", "小红", "小刚"}
# if "小明" in students:
#     print("小明在集合中")

# 列表、元组、字典和集合的对比
# 列表：有序，可以重复，支持索引，可以修改。
# 元组：有序，可以重复，支持索引，不能修改元素。
# 字典：通过key访问value，可以修改，适合保存对应关系。
# 集合：元素不重复，不支持索引，主要用于成员判断和集合关系。
# 集合不提供像列表一样的索引位置，不能依赖集合的遍历顺序。

# Python与C语言的区别
# C语言没有与Python集合完全对应的内置基础容器。
# Python集合不需要手动管理内存，也不需要自己实现基础去重逻辑。
# 集合不是数组，不能使用set_data[0]像访问数组或列表一样访问元素。
# 集合更强调元素是否存在，以及集合之间的关系。

# 综合案例：集合、for和if
# numbers = {10, 15, 20, 25, 30}
# for number in numbers:
#     if number >= 20:
#         print(f"符合条件的数字：{number}")

# 集合可以保存不重复的数据，并用于成员判断和集合关系处理。
# 后续还会学习不同数据容器的综合使用。
