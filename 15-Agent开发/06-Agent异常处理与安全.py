# Agent异常处理与安全

# Agent比普通LLM程序多了一层工具执行，因此需要额外关注安全。

# 工具执行可能因为参数错误或函数内部问题失败：
# def divide(a, b):
#     if b == 0:
#         raise ValueError("除数不能为0")
#     return a / b

# 处理工具调用时，可以捕获工具的明确异常：
# try:
#     result = divide(arguments["a"], arguments["b"])
# except ValueError as e:
#     result = f"工具执行失败：{e}"

# 不能完全相信模型提供的参数。
# Python程序应该检查参数类型、取值范围和业务规则。

# Agent必须设置最大执行次数：
# max_steps = 5
#
# for step in range(max_steps):
#     ...

# 工具白名单表示：Agent只能调用程序明确提供的工具。
# 不应该让模型任意执行Python代码或系统命令。

# 本章禁止把下面内容作为工具：
# os.system(...)
# subprocess.run(...)
# 任意文件删除、任意数据库写入和执行用户提供的代码。

# 当前只学习基础异常处理、参数验证、最大步数和工具白名单。
# 这条链路可以概括为：Python Exception → API Error → Tool Error → Agent Failure。
# 不同层负责处理自己的错误，Agent再把明确的失败结果反馈给用户或模型。
