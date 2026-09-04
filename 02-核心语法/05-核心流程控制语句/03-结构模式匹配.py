#结构模式匹配结构是match-case语句的核心，match-case语句是Python 3.10引入的一种新的控制流结构，用于模式匹配。结构模式匹配允许我们根据对象的结构和内容来进行条件判断和分支处理。
#基本语法：
# match subject:  # subject是要匹配的对象，可以是任何类型的对象
#     case "pattern1":  # 这里匹配字符串字面量；模式还可以是序列、字典等结构
#         pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系
#     case 2:  # 数字字面量示例；未加引号的名称通常表示捕获变量，会匹配并绑定值
#         pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系
#     case "pattern3" | "pattern4":  # |表示或，匹配pattern3或pattern4
#         pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系
#     case _:  # _ 是兜底模式，可以匹配前面没有匹配到的所有情况
#         pass  # 执行代码逻辑；此部分每行前面要缩进来描述代码的层级关系


#案例1:工作日程安排
# day = input("请输入今天是星期几（1 - 7）：")

# match day:
#     case "1":
#         print("今天是星期一，安排工作任务A")
#     case "2":
#         print("今天是星期二，安排工作任务B")
#     case "3":
#         print("今天是星期三，安排工作任务C")
#     case "4":
#         print("今天是星期四，安排工作任务D")
#     case "5":
#         print("今天是星期五，安排工作任务E")
#     case "6" | "7":
#         print("今天是周末，安排休息和娱乐活动")
#     case _:
#         print("输入的星期几不合法，请输入1到7之间的数字")


#案例2:基于match...case语句实现一个计算器，可以实现+-*/四则运算
# num1 = float(input("请输入第一个数字："))
# operator = input("请输入运算符（+、-、*、/）：")
# num2 = float(input("请输入第二个数字："))

# match operator:
#     case "+":
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#     case "-":
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#     case "*":
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"{num1} / {num2} = {result}")
#         else:
#             print("除数不能为零，请重新输入！")
#     case _:
#         print("输入的运算符不合法，请输入+、-、*、/")
