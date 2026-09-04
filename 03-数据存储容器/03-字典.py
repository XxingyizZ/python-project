# 字典是数据容器的一类，可以保存多个键值对
# 字典中的每一组数据由key和value组成。
# key用于定位数据，value是实际保存的数据。
# 一个key对应一个value，同一个字典中的key应该具有唯一性。
# value可以是不同类型的数据，也可以是列表、元组或其他字典。
# 字典是可变对象，可以进行增删改查。

# 字典的创建
# 字典使用大括号定义，每组key和value之间使用冒号分隔，不同键值对之间使用逗号分隔。
# student = {
#     "name": "小明",
#     "age": 18,
#     "score": 90
# }
# print(student)

# 空字典可以使用一对空的大括号表示。
# empty_dict = {}
# print(empty_dict)

# 常见的key可以使用字符串，整数也可以作为key。
# scores = {
#     1: 85,
#     2: 92
# }
# print(scores[1])

# dict()也可以创建空字典，但当前阶段优先掌握大括号的写法。
# empty_dict = dict()

# 字典的读取
# 字典主要通过key访问对应的value，而不是像列表一样通过整数索引访问。
# student = {"name": "小明", "age": 18}
# print(student["name"])
# print(student["age"])

# 使用不存在的key访问value时，会产生KeyError。
# 列表使用不存在的索引会产生IndexError，字典和列表的错误类型不同。

# get()可以读取指定key对应的value。
# key不存在时，get()默认返回None，也可以指定默认值。
# student = {"name": "小明", "age": 18}
# print(student.get("name"))
# print(student.get("gender"))
# print(student.get("gender", "未知"))

# 字典的修改和新增
# key已经存在时，赋值会修改对应的value。
# key不存在时，赋值会新增一个键值对。
# student = {"name": "小明", "age": 18}
# student["age"] = 19       # 修改已有的value
# student["score"] = 90     # 新增键值对
# print(student)

# 删除字典元素
# del可以删除指定的键值对。
# student = {"name": "小明", "age": 18, "score": 90}
# del student["age"]
# print(student)

# pop()可以删除指定的键值对，并返回被删除的value。
# student = {"name": "小明", "age": 18, "score": 90}
# removed_score = student.pop("score")
# print(removed_score)
# print(student)

# 使用del或pop()删除不存在的key时，会产生KeyError。

# len()函数
# len()获取的是字典中键值对的数量。
# student = {"name": "小明", "age": 18, "score": 90}
# print(len(student))  # 3

# 字典成员判断
# 直接对字典使用in，默认判断的是key，而不是value。
# student = {"name": "小明", "age": 18}
# print("name" in student)  # True
# print("小明" in student)  # False
# print("小明" in student.values())  # True
# print("gender" not in student)  # True

# 遍历字典
# 直接使用for遍历字典时，循环变量依次得到的是key。
# student = {"name": "小明", "age": 18, "score": 90}
# for key in student:
#     print(key)

# keys()可以用于遍历所有key。
# for key in student.keys():
#     print(key)

# values()可以用于遍历所有value。
# for value in student.values():
#     print(value)

# items()可以同时取得key和value。
# key和value只是普通变量名，不是Python关键字。
# for key, value in student.items():
#     print(f"{key}：{value}")

# 字典与if条件判断
# scores = {
#     "小明": 85,
#     "小红": 92,
#     "小刚": 58
# }
# for name, score in scores.items():
#     if score >= 60:
#         print(f"{name}：{score}")

# 字典常见方法
# get()读取value，key不存在时可以返回默认值。
# keys()获取所有key，values()获取所有value。
# items()获取所有key和value，pop()删除键值对并返回被删除的value。
# update()可以批量修改或新增键值对。
# student = {"name": "小明", "age": 18}
# student.update({"age": 19, "score": 90})
# print(student)

# 嵌套字典
# 字典的value可以是另一个字典。
# student = {
#     "name": "小明",
#     "info": {
#         "age": 18,
#         "score": 90
#     }
# }
# print(student["info"])
# print(student["info"]["age"])

# 编号可以对应一名学生的信息。
# students = {
#     "001": {"name": "小明", "age": 18},
#     "002": {"name": "小红", "age": 19}
# }
# for student_id, student_info in students.items():
#     print(student_id, student_info["name"])

# 列表和字典
# 列表可以保存多条数据，字典可以描述一条数据的多个属性。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 58}
# ]
# for student in students:
#     print(student["name"], student["score"])

# 列表、字典、for和if可以结合处理一组数据。
# for student in students:
#     if student["score"] >= 60:
#         print(f"{student['name']}及格")
#     else:
#         print(f"{student['name']}不及格")

# 列表、元组和字典的对比
# 列表和元组主要通过索引访问元素，字典主要通过key访问value。
# list_data = ["小明", 18]
# tuple_data = ("小明", 18)
# dict_data = {"name": "小明", "age": 18}
# print(list_data[0])
# print(tuple_data[0])
# print(dict_data["name"])

# 列表：有序，可以修改元素。
# 元组：有序，不能修改元素。
# 字典：通过key访问value，可以修改键值对，适合保存具有对应关系的数据。

# 综合案例：字典、for和if
# scores = {"小明": 85, "小红": 92, "小刚": 58}
# for name, score in scores.items():
#     if score >= 60:
#         print(f"{name}及格")
#     else:
#         print(f"{name}不及格")

# 综合案例：列表、字典、for和if
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 58}
# ]
# passed_count = 0
# for student in students:
#     if student["score"] >= 60:
#         passed_count += 1
#         print(f"{student['name']}的成绩是{student['score']}，及格")
# print(f"及格人数：{passed_count}")

# 字典可以使用key和value组织具有对应关系的数据。
# 后续还会继续学习其他常见的数据容器。
