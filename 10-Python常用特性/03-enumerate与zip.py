# enumerate()与zip()

# enumerate()可以在遍历可迭代对象时，同时取得索引和元素。
# students = ["小明", "小红", "小刚"]
# for index in range(len(students)):
#     print(index, students[index])
#
# for index, student in enumerate(students):
#     print(index, student)

# enumerate()的基本结构：enumerate(可迭代对象)
# start可以指定索引的起始值。
# for index, student in enumerate(students, start=1):
#     print(index, student)

# zip()可以把多个可迭代对象按位置配对。
# names = ["小明", "小红", "小刚"]
# scores = [85, 90, 72]
# for name, score in zip(names, scores):
#     print(name, score)

# 当参与zip()的对象长度不同时，会按照较短的对象停止配对。
# names = ["小明", "小红", "小刚"]
# scores = [85, 90]
# for name, score in zip(names, scores):
#     print(name, score)

# enumerate()和zip()可以组合使用。
# names = ["小明", "小红", "小刚"]
# scores = [85, 58, 72]
# for index, (name, score) in enumerate(zip(names, scores), start=1):
#     if score >= 60:
#         print(index, name, score)

# enumerate()和zip()可以让遍历多个相关数据时的代码更清晰。
