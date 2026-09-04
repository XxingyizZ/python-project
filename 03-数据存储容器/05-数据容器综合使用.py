# 数据容器综合使用
# 本章不学习新的数据容器，主要组合使用已经学习过的列表、元组、字典和集合。

# 一、如何选择数据容器
# 列表通常适合保存多条有顺序的数据，可以重复，也支持索引访问。
# 元组通常适合保存固定结构的数据，创建后不能修改元素。
# 字典适合描述一条数据的多个属性，使用key访问对应的value。
# 集合适合保存不重复的数据，也适合成员判断和集合关系。
# 下面的示例用于回忆四种容器的主要特点。
# names = ["小明", "小红", "小明"]
# point = (10, 20)
# student = {"name": "小明", "age": 18}
# unique_names = {"小明", "小红"}

# 二、列表和字典
# 列表负责保存多条数据，每个字典负责描述一条数据。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 58}
# ]

# 先通过列表索引取得一个字典，再通过字典key取得value。
# print(students[0]["name"])

# 使用for循环遍历列表中的每个字典。
# for student in students:
#     print(student["name"])

# 三、列表、字典、for和if
# 根据成绩筛选及格学生。
# for student in students:
#     if student["score"] >= 60:
#         print(f"{student['name']}及格")

# 也可以筛选不及格学生。
# for student in students:
#     if student["score"] < 60:
#         print(f"{student['name']}不及格")

# 四、列表和集合
# 列表可以保存原始数据，集合可以得到不重复的数据。
# numbers = [1, 2, 2, 3, 3, 4]
# unique_numbers = set(numbers)
# print(unique_numbers)

# 学生姓名去重。
# students = ["小明", "小红", "小明", "小刚"]
# unique_students = set(students)
# print(unique_students)

# 五、字典和列表
# 字典可以保存一条数据的多个属性，value也可以是列表。
# student = {
#     "name": "小明",
#     "scores": [85, 90, 88]
# }
# print(student["scores"])
#
# for score in student["scores"]:
#     print(score)

# 六、字典和嵌套数据
# 外层字典通过编号对应学生信息，内层字典保存学生属性，列表保存多项成绩。
# students = {
#     "001": {
#         "name": "小明",
#         "scores": [85, 90, 88]
#     },
#     "002": {
#         "name": "小红",
#         "scores": [92, 95, 90]
#     }
# }

# 通过多层key访问数据。
# print(students["001"]["name"])
# print(students["001"]["scores"])

# 遍历外层字典，读取内层字典中的姓名。
# for student_id, student_info in students.items():
#     print(student_id, student_info["name"])

# 七、集合关系综合
# 复用集合已经学习过的并集、交集和差集运算。
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

# 八、嵌套for循环
# 列表中保存多个字典，字典中的value保存成绩列表。
# students = [
#     {
#         "name": "小明",
#         "scores": [85, 90, 88]
#     },
#     {
#         "name": "小红",
#         "scores": [92, 95, 90]
#     }
# ]
#
# for student in students:
#     print(f"{student['name']}的成绩：")
#
#     for score in student["scores"]:
#         print(score)

# 九、简单统计
# 统计成绩列表中及格学生的数量。
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 58}
# ]
# passed_count = 0
#
# for student in students:
#     if student["score"] >= 60:
#         passed_count += 1
#
# print(f"及格人数：{passed_count}")

# 统计列表中不重复数据的数量。
# numbers = [1, 2, 2, 3, 3, 4]
# unique_numbers = set(numbers)
# print(f"不重复数据数量：{len(unique_numbers)}")

# 十、综合案例：列表、字典、for和if
# students = [
#     {"name": "小明", "score": 85},
#     {"name": "小红", "score": 92},
#     {"name": "小刚", "score": 58}
# ]
# passed_count = 0
#
# for student in students:
#     if student["score"] >= 60:
#         passed_count += 1
#         print(f"{student['name']}及格")
#     else:
#         print(f"{student['name']}不及格")
#
# print(f"及格人数：{passed_count}")

# 十一、综合案例：列表、字典、列表和嵌套for
# students = [
#     {
#         "name": "小明",
#         "scores": [85, 90, 88]
#     },
#     {
#         "name": "小红",
#         "scores": [92, 95, 90]
#     }
# ]
#
# for student in students:
#     print(f"{student['name']}的成绩：")
#
#     for score in student["scores"]:
#         print(score)

# 十二、四种容器总结
# 列表：通常用于保存多条有顺序的数据，可以重复，支持索引。
# 元组：通常用于保存固定结构的数据，支持索引，不能修改元素。
# 字典：保存key和value的对应关系，通过key访问value。
# 集合：保存不重复的元素，适合成员判断和集合关系。
#
# list_data = ["小明", 18]
# tuple_data = ("小明", 18)
# dict_data = {"name": "小明", "age": 18}
# set_data = {"小明", "小红"}
#
# print(list_data[0])
# print(tuple_data[0])
# print(dict_data["name"])
# print("小明" in set_data)

# 本章重点：列表和字典是常见的组合，列表和集合可以用于去重，
# 字典和列表可以保存一条数据中的多个列表数据，多种容器也可以嵌套组合。
# 后续将继续学习函数，并使用函数封装重复的数据处理逻辑。
