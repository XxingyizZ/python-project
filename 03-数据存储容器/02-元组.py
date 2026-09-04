# 元组是数据容器的一类，可以一次性存储多个元素
# 定义：元组名称 = (元素1, 元素2, 元素3, ...)
# 元组的特点：
# 1. 元组中的元素可以是任意类型的数据
# 2. 元组中的元素是有序的，可以通过索引访问
# 3. 元组创建后不能修改其中的元素
# 4. 元组可以嵌套，即元组中可以包含其他元组

# 元组的创建
# 元组中的元素使用逗号分隔，通常使用圆括号表示。
# colors = ("红色", "绿色", "蓝色")
# student = ("小明", 18, 90.5)
# print(colors)
# print(student)

# 空元组
# 空元组可以使用一对空的圆括号表示。
# empty_tuple = ()
# print(empty_tuple)

# 单元素元组
# 单元素元组中的逗号不能省略。
# number = (10,)
# print(number)

# (10)不是元组，而是数字10外面加了一对圆括号。
# number = (10)
# print(type(number))  # <class 'int'>

# (10,)才是单元素元组，区分单元素元组的关键是逗号。
# number = (10,)
# print(type(number))  # <class 'tuple'>

# 也可以写成number = 10,，但初学时建议使用number = (10,)。

# 元组索引
# 元组同样支持索引访问，索引规则与列表相同。
# colors = ("红色", "绿色", "蓝色")
# print(colors[0])
# print(colors[2])

# 负数索引
# 负数索引可以从元组末尾开始访问元素。
# colors = ("红色", "绿色", "蓝色")
# print(colors[-1])  # 蓝色
# print(colors[-3])  # 红色

# 使用不存在的索引访问元组元素时，会产生IndexError。
# 因此，访问元素时要确保索引没有超出元组的有效范围。

# 元组切片
# 元组同样支持切片，切片规则与列表相同。
# 切片语法：序列[开始索引:结束索引:步长]
# 切片结果仍然是一个元组。
# numbers = (0, 1, 2, 3, 4, 5)
# print(numbers[1:4])  # (1, 2, 3)
# print(numbers[::2])  # (0, 2, 4)

# len()函数
# len()函数可以获取元组中元素的数量。
# student = ("小明", 18, 90.5)
# print(len(student))

# 遍历元组
# for循环可以依次取出元组中的每个元素。
# fruits = ("苹果", "香蕉", "橙子")
# for fruit in fruits:
#     print(fruit)

# 成员判断
# in可以判断元素是否存在于元组中，not in可以判断元素是否不存在于元组中。
# 判断结果是布尔值True或False。
# fruits = ("苹果", "香蕉", "橙子")
# print("香蕉" in fruits)      # True
# print("西瓜" not in fruits)  # True

# 元组与if条件判断
# scores = (56, 78, 90, 45, 88)
# for score in scores:
#     if score >= 60:
#         print(score)

# 元组的不可变性
# 元组创建后不能通过索引修改其中的元素。
# numbers = (10, 20, 30)
# numbers[0] = 100  # 会产生TypeError

# 列表创建后可以通过索引修改元素，元组不能这样修改。
# list_numbers = [10, 20, 30]
# list_numbers[0] = 100
# print(list_numbers)  # [100, 20, 30]
#
# tuple_numbers = (10, 20, 30)
# tuple_numbers[0] = 100  # 会产生TypeError

# 元组不能使用列表中用于修改数据的方法，例如append()、insert()、remove()和pop()。
# 元组中的元素不能被重新赋值，但如果元素本身是可变对象，相关内容留到后续再学习。

# 元组的常见方法
# count()用于统计指定值在元组中出现的次数。
# numbers = (1, 2, 2, 3, 2)
# print(numbers.count(2))  # 3

# index()返回第一个匹配元素的索引。
# fruits = ("苹果", "香蕉", "橙子")
# print(fruits.index("香蕉"))  # 1

# 如果index()找不到指定元素，会产生ValueError。

# 嵌套元组
# 元组中的元素也可以是元组。
# scores = (
#     (80, 90, 85),
#     (70, 88, 92)
# )
# print(scores[0])     # (80, 90, 85)
# print(scores[0][1])  # 90

# 使用嵌套for循环遍历嵌套元组。
# for row in scores:
#     for score in row:
#         print(score)

# 基础元组解包
# 可以把元组中的元素依次赋值给多个变量。
# point = (10, 20)
# x, y = point
# print(x)
# print(y)

# 当前只需要掌握基础的元组解包，复杂解包方式留到后续学习。

# 列表与元组的对比
# 列表和元组都可以保存多个元素，都有顺序，都支持索引、切片、遍历和成员判断。
# list_data = [10, 20, 30]
# tuple_data = (10, 20, 30)
#
# 列表是可变的，可以修改元素。
# list_data[0] = 100
# print(list_data)  # [100, 20, 30]
#
# 元组是不可变的，不能通过索引修改元素。
# tuple_data[0] = 100  # 会产生TypeError

# 如果数据需要频繁修改，通常更适合使用列表；
# 如果数据创建后不希望被修改，可以考虑使用元组。

# 综合案例：遍历元组，筛选并统计及格成绩
# scores = (78, 92, 65, 88, 56)
# passed_count = 0
#
# for score in scores:
#     if score >= 60:
#         print(f"及格成绩：{score}")
#         passed_count += 1
#
# print(f"及格人数：{passed_count}")

# 综合案例：遍历嵌套元组中的成绩
# scores = (
#     (80, 90, 85),
#     (70, 88, 92)
# )
#
# for row in scores:
#     for score in row:
#         if score >= 90:
#             print(f"优秀成绩：{score}")
