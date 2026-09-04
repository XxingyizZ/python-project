# #算术运算符
# print(10 + 5)  # 加法
# print(10 - 5)  # 减法
# print(10 * 5)  # 乘法
# print(10 / 5)  # 除法，结果是浮点数
# print(10 // 5) # 地板除（整除），结果为 2 #如果操作数包含浮点数，结果也可能是 float；结果会向负无穷取整
# print(10 % 3)  # 取余数
# print(2 ** 3)  # 幂运算，2的3次方

#算术运算符的优先级 ** -> * / // % -> + -；除幂运算外，同级运算符通常从左到右计算，幂运算从右到左计算


# #案例:输入两个数，计算它们的和与差
# x = float(input("请输入x的值："))
# y = float(input("请输入y的值："))
# print(f"x + y = {x + y}")
# print(f"x - y = {x - y}")


#赋值运算符
z = 10
z += 5  # 等价于 z = z + 5
z -= 3  # 等价于 z = z - 3
z *= 2  # 等价于 z = z * 2
z /= 4  # 等价于 z = z / 4
z //= 2 # 等价于 z = z // 2
z %= 3  # 等价于 z = z % 3
z **= 2 # 等价于 z = z ** 2

# #比较运算符 比较计算两边的表达式，返回布尔值 True 或 False
# print(10 > 5)   # 大于
# print(10 < 5)   # 小于
# print(10 >= 5)  # 大于等于
# print(10 <= 5)  # 小于等于
# print(10 == 5)  # 等于
# print(10 != 5)  # 不等于

# 逻辑运算符通常用于组合条件。
# not 总是返回 True 或 False；and 和 or 会根据短路规则返回某个操作数。
#例如
# print(1 and 2)  # 2
# print(0 or 5)   # 5
# print(True and False)  # 与
# print(True or False)   # 或
# print(not True)        # 非
