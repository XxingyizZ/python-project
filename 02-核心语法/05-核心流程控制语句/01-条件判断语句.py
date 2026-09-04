#if条件判断：只有满足条件才会执行对应的代码逻辑

# if condition:  # Python 会根据条件表达式的真值进行判断，结尾不要忘记加冒号
#     pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系
# else:  #如果条件不满足，则执行else后面的代码逻辑，结尾同样有冒号
#    pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系

#执行代码逻辑可以写成pass， pass表示占位符，什么都不做，通常用于占位，后续再补充代码逻辑

# 案例1：登陆账号密码判断

# #正确的账号密码
# correct_username = "admin"
# correct_password = "123456"

# # 用户输入账号密码
# username = input("请输入账号：")
# password = input("请输入密码：")

# #判断账号密码是否正确
# if username == correct_username and password == correct_password:
#     print("登录成功！")
# else:
#     print("账号或密码错误，请重新输入！")


#进阶if语句：if elif else

# #案例2：判断一个数是正数、负数或者0
# num = int(input("请输入要判断的是数字"))

# if num > 0:
#     print(f"{num}是一个正数")
# elif num < 0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}是0")


# #案例3: 输入三个数，判断三边能不能构成三角形， 如果能构成三角形，判断是等边三角形、等腰三角形还是普通三角形
# a = float(input("请输入第一条边的长度："))
# b = float(input("请输入第二条边的长度："))
# c = float(input("请输入第三条边的长度："))

# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("这是一个等边三角形")
#     elif a == b or a == c or b == c:
#         print("这是一个等腰三角形")
#     else:
#         print("这是一个普通三角形")
# else:
#     print("这三条边不能构成三角形")
