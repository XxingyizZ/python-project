# 列表是数据容器的一类，可以一次性存储多个元素
# 定义：列表名称 = [元素1, 元素2, 元素3, ...]
#列表的特点：
#1. 列表中的元素可以是任意类型的数据，即同一个列表可以存储不同类型的数据
#2. 列表中的元素是有序的，可以通过索引访问，索引从0开始，负数索引表示从列表末尾开始访问
#3. 列表是可变的，可以对列表进行增删改查等
#4. 列表可以嵌套，即列表中可以包含其他列表

# 列表的创建和基本读取
# 空列表可以使用一对方括号表示，列表中的元素使用逗号分隔。
# 一个列表可以存储相同类型或不同类型的数据。
# fruits = ["苹果", "香蕉", "橙子"]
# student = ["小明", 18, 90.5]
# empty_list = []
# print(fruits)
# print(student)

# 访问列表元素
# 列表中的元素可以通过索引访问，索引从0开始。
# 正数索引从列表开头开始计算，负数索引从列表末尾开始计算。
# fruits = ["苹果", "香蕉", "橙子"]
# print(fruits[0])  # 苹果
# print(fruits[2])  # 橙子
# print(fruits[-1]) # 橙子
# print(fruits[-3]) # 苹果

# 使用不存在的索引访问列表元素时，会产生IndexError。
# 因此，访问元素时要确保索引没有超出列表的有效范围。

# 修改列表元素
# 列表是可变的，可以通过索引修改指定位置的元素。
# fruits = ["苹果", "香蕉", "橙子"]
# fruits[1] = "葡萄"
# print(fruits)  # ["苹果", "葡萄", "橙子"]

# len()函数可以获取列表中元素的数量。
# fruits = ["苹果", "香蕉", "橙子"]
# print(len(fruits))
# print(fruits[len(fruits) - 1])  # 访问最后一个元素

# 列表切片
# 切片：从序列中截取一部分数据。
# 
# 语法：
# 序列[开始索引:结束索引:步长]
# 
# 特点：
# 1. 左闭右开：包含开始索引，不包含结束索引。
# 2. 步长默认为 1。
# 3. 开始索引、结束索引、步长都可以省略。
# 4. 开始索引和结束索引可以使用负数索引；步长为负数时可以从右向左截取。
# 5. 步长 > 0：从左向右截取；步长 < 0：从右向左截取。

# lst = [0, 1, 2, 3, 4, 5]
# print(lst[1 : 4]) # [1, 2, 3]
# print(lst[0: 5 : 2]) #[0, 2, 4]

# 列表遍历
# for循环可以依次取出列表中的每个元素。
# fruits = ["苹果", "香蕉", "橙子", "葡萄"]
# for fruit in fruits:
#     print(fruit)

# 列表与if条件判断
# numbers = [3, 8, 12, 5, 7]
# for number in numbers:
#     if number > 6:
#         print(number)

# 成员判断
# in可以判断元素是否存在于列表中，not in可以判断元素是否不存在于列表中。
# 判断结果是布尔值True或False。
# fruits = ["苹果", "香蕉", "橙子"]
# print("香蕉" in fruits)       # True
# print("西瓜" not in fruits)   # True

# name = "小明"
# names = ["小明", "小红", "小刚"]
# if name in names:
#     print("姓名在列表中")
# else:
#     print("姓名不在列表中")

#列表常见方法:
#append():在列表末尾追加元素，直接修改原列表，通常返回None。s.append(10086)
#insert():在指定索引之前插入元素，直接修改原列表，通常返回None。s.insert(0, 92)
#remove():删除列表中第一个匹配到的值，直接修改原列表，通常返回None。s.remove(75)
# pop(): 删除指定索引位置的元素，并返回被删除的元素；如果未指定索引，默认删除最后一个元素
# 例如：s.pop(0)
# 例如：s.pop()
# sort(): 按原地方式对列表排序，直接修改原列表，通常返回None；列表中的元素需要支持相互比较
# 例如：s.sort()
#reverse():倒置列表，直接修改原列表，通常返回None。s.reverse()

# 列表常见方法案例
# append()会在列表末尾添加一个元素。
# append()会直接修改原列表。
# fruits = ["苹果", "香蕉"]
# fruits.append("橙子")
# print(fruits)  # ["苹果", "香蕉", "橙子"]

# insert()会在指定索引之前插入一个元素。
# fruits = ["苹果", "香蕉"]
# fruits.insert(1, "橙子")
# print(fruits)  # ["苹果", "橙子", "香蕉"]

# remove()根据值删除列表中第一个匹配到的元素。
# fruits = ["苹果", "香蕉", "苹果"]
# fruits.remove("苹果")
# print(fruits)  # ["香蕉", "苹果"]

# pop()根据索引删除元素，并返回被删除的元素。
# fruits = ["苹果", "香蕉", "橙子"]
# removed_fruit = fruits.pop(1)
# print(removed_fruit)  # 香蕉
# print(fruits)         # ["苹果", "橙子"]

# 不指定索引时，pop()默认删除最后一个元素。
# last_fruit = fruits.pop()
# print(last_fruit)
# print(fruits)

# sort()默认按照升序对列表进行排序，会直接修改原列表。
# numbers = [5, 2, 8, 1, 3]
# numbers.sort()
# print(numbers)  # [1, 2, 3, 5, 8]

# reverse()会直接将列表中的元素倒置。
# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)  # [5, 4, 3, 2, 1]

# 嵌套列表
# 列表中的元素也可以是列表。下面的列表可以看作两组成绩。
# scores = [
#     [80, 90, 85],
#     [70, 88, 92]
# ]
# print(scores[0])     # [80, 90, 85]
# print(scores[0][1])  # 90

# 使用嵌套for循环遍历嵌套列表。
# for row in scores:
#     for score in row:
#         print(score)

# 综合案例：遍历列表，筛选并统计偶数
# numbers = [1, 4, 7, 10, 13, 16]
# even_count = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         print(f"偶数：{number}")
#         even_count += 1
#
# print(f"偶数的数量是：{even_count}")

# 综合案例：处理成绩列表
# scores = [78, 92, 65, 88, 56]
# scores.append(95)
# scores[2] = 75
#
# print("所有成绩：")
# for score in scores:
#     print(score)
#
# print("及格成绩：")
# for score in scores:
#     if score >= 60:
#         print(score)
#
# scores.sort()
# print("从低到高排序后的成绩：", scores)

# 列表可以保存和处理一组数据。后续还会继续学习其他常见的数据容器。
