# #获取键盘上的数据
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# print(f"你的名字是：{name}")
# print(f"你的年龄是：{age}")

# #数据类型转化
# #从键盘上获取的数据都是字符串类型，如果需要进行数学运算，需要将其转化为数值类型
# x = input("请输入x的值：")
# y = input("请输入y的值：")
# #将字符串类型转化为整数类型
# print(f"x + y = {int(x) + int(y)}")

#注意，输出换行用\n，print()函数默认输出后会换行，如果不想换行，可以在print()函数中添加end参数，指定输出结束后的字符，默认为换行符\n
print("Hello, World!", end="\n")
print("Hello", end=" ")
print("World!", end=" ")