# 配置与环境变量

# 程序运行时经常需要一些配置，例如：
# 程序名称、服务器地址、端口和API地址。

# 配置是程序运行时需要使用、但不应该全部写死在业务代码中的信息。

# os模块可以读取环境变量。
# import os
#
# value = os.getenv("MY_CONFIG")
# print(value)

# 环境变量由运行环境提供，Python程序可以读取它们。
# 如果环境变量不存在，os.getenv()默认会得到None。

# 不应该把真实的密码、API Key或Token直接写进代码：
# api_key = "真实的密钥"

# 可以使用环境变量保存这类配置：
# import os
# api_key = os.getenv("API_KEY")

# .env是很多项目用于保存本地环境变量配置的文件形式。
# 当前只做认识，不引入python-dotenv，也不实现.env自动加载。

# 密码、API Key和Token等敏感信息通常不应该提交到公开Git仓库。
# 本章不连接任何API，只学习基础配置安全意识。
