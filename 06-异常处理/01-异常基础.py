# 异常基础
# 程序运行过程中出现无法正常完成当前操作的问题时，Python可能产生异常。
# 异常是运行过程中发生的问题，不等同于代码本身的语法错误。

# 运行时异常：代码语法正确，但运行过程中出现问题。
# print(10 / 0)  # ZeroDivisionError
# numbers = [1, 2, 3]
# print(numbers[10])  # IndexError

# 语法错误：代码不符合Python语法，程序无法正常执行。
# if True
#     print("你好")

# 语法错误和运行时异常的区别：
# 语法错误：代码写法不符合语法规则。
# 运行时异常：代码运行到某一步时出现了问题。

# 常见异常与前面知识的联系：
# 运算中除数为0：ZeroDivisionError
# 列表索引超出范围：IndexError
# 字典中不存在指定key：KeyError
# 数据类型操作不匹配：TypeError
# 类型转换时数据内容不合法：ValueError

# 异常可能导致程序提前停止，后续内容不会继续执行。
