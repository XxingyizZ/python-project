# 函数返回值
# return可以把函数处理后的结果返回给调用者。

# 使用return返回一个结果。
# def add(a, b):
#     return a + b
#
# result = add(10, 20)
# print(result)

# 返回值可以保存到变量中，也可以继续参与计算。
# def multiply(a, b):
#     return a * b
#
# result = multiply(3, 4)
# print(result + 1)

# print()负责输出内容，return负责把结果返回给调用者。
# def add_with_print(a, b):
#     print(a + b)
#
# def add_with_return(a, b):
#     return a + b
#
# add_with_print(10, 20)  # 函数内部直接输出结果
# result = add_with_return(10, 20)
# print(result)            # 接收函数返回的结果

# 函数没有显式return时，调用结果通常是None。
# def greet():
#     print("你好")
#
# result = greet()
# print(result)  # None

# 执行到return后，当前函数会结束，后面的代码不会执行。
# def test():
#     return 10
#     print("这行不会执行")
#
# print(test())

# return可以配合if，根据不同条件返回不同结果。
# def check_score(score):
#     if score >= 60:
#         return "及格"
#     return "不及格"
#
# print(check_score(80))
# print(check_score(50))

# 函数可以返回列表等数据容器。
# def get_even_numbers(numbers):
#     even_numbers = []
#
#     for number in numbers:
#         if number % 2 == 0:
#             even_numbers.append(number)
#
#     return even_numbers
#
# numbers = [1, 2, 3, 4, 5, 6]
# print(get_even_numbers(numbers))
