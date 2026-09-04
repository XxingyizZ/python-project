# API基础

# API是程序之间进行交互的一种接口。
# 本章重点学习Web API，也就是通过HTTP访问的API。

# 浏览器访问网页，结果通常主要面向人阅读。
# 程序访问API，结果通常主要面向程序处理。

# API Endpoint可以简单理解为程序请求的具体API地址。
# https://example.com/api/users

# API请求中常见的信息：
# Query参数 → 放在URL中的查询条件
# Body       → 请求中提交的数据
# Header     → 请求的附加信息

# 某些API需要身份认证，例如API Key或Token。
# 真实密钥不能直接写进代码，可以从环境变量读取：
# import os
# api_key = os.getenv("API_KEY")

# 本章不使用真实密钥，也不访问需要注册的业务API。
