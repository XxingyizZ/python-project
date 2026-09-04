# #While循环的语法结构
# while 条件表达式:
#     pass  # 循环体语句1
#     pass  # 循环体语句2
#     ...
# else:   # 循环正常结束、没有执行 break 时执行一次，else 语句可省略
#     pass  # 循环体语句3
#     pass  # 循环体语句4
#     ...


#案例1:打印十遍“人生苦短，我用python”
# count = 0
# while count < 10:
#     print("人生苦短，我用python")
#     count += 1
# else:
#     print("循环结束")



#案例2:基于while循环计算1到100的所有偶数累加和
# sum_even = 0
# num = 2
# while num <= 100:
#     sum_even += num
#     num += 2
# print("1到100的所有偶数累加和为：", sum_even)


#for循环本质是一种遍历，会对可迭代对象中的每个元素执行循环体语句，直到遍历完所有元素为止。for循环的语法结构如下：
# for 变量 in 可迭代对象:
#     pass  # 循环体语句1
#     pass  # 循环体语句2
#     ...
# else:   # 循环正常结束、没有执行 break 时执行一次，else 语句可省略
#     pass  # 循环体语句3
#     pass  # 循环体语句4
#     ...


#列表是后续“数据存储容器”章节中会详细学习的一种可迭代对象。
#这里先使用列表作为for循环遍历的直观示例，当前只需要理解：for会依次取出列表中的每个元素。
#案例3:使用for循环遍历列表中的元素
# fruits = ["苹果", "香蕉", "橙子", "葡萄"]
# for fruit in fruits:
#     print(fruit)


#range()函数是Python内置的一个函数，用于生成一个整数序列，常用于for循环中。它的语法结构如下：
#范围都是左闭右开区间，即包含起始值但不包含结束值。
# range(stop)  # 生成从0到stop-1的整数序列
# range(start, stop)  # 生成从start到stop-1的整数序列
# range(start, stop, step)  # 从 start 开始，按 step 递增或递减，直到到达 stop 前停止；stop 不包含


#案例5:基于for循环计算1到100的所有奇数累加和
# sum_odd = 0
# for num in range(1, 101, 2):
#     sum_odd += num
# print("1到100的所有奇数累加和为：", sum_odd)


#案例6:基于for循环，根据输入的长方形的长度m和宽度n，打印出一个由“*”组成的长方形
# m = int(input("请输入长方形的长度m："))
# n = int(input("请输入长方形的宽度n："))
# for i in range(m):
#     for j in range(n):
#         print("*", end=" ")
#     print()  # 换行


#案例7:基于for循环，打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={i*j}", end="\t")
#     print()  # 换行
