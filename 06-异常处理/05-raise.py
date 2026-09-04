# raise
# raise可以在程序中主动产生一个异常。

# def check_age(age):
#     if age < 0:
#         raise ValueError("年龄不能小于0")
#     return age
#
# print(check_age(18))

# 可以在调用函数时捕获主动产生的异常。
# def check_score(score):
#     if score < 0 or score > 100:
#         raise ValueError("成绩应该在0到100之间")
#     return score
#
# try:
#     print(check_score(120))
# except ValueError as e:
#     print(e)

# raise适合在发现数据不符合要求时主动报告问题。
# 当前阶段只学习raise的基础作用，不学习自定义异常类。
