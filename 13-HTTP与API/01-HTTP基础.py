# HTTP基础

# HTTP是客户端和服务器之间进行通信的一种协议。
# 客户端可以是浏览器，也可以是Python程序。

# 一次基本通信过程：
# 客户端 → 请求（Request）→ 服务器
# 客户端 ← 响应（Response）← 服务器

# 请求通常包含：请求方法、URL、请求头和请求数据。
# 响应通常包含：状态码、响应头和响应数据。

# URL示例：
# https://example.com/users
# https       → 协议
# example.com → 域名
# /users      → 路径

# 常见HTTP方法：
# GET    → 获取数据
# POST   → 提交数据
# PUT    → 更新数据
# DELETE → 删除数据
# 本章重点学习GET和POST。

# API经常使用JSON作为数据交换格式。
# HTTP负责通信，JSON负责表示和传递结构化数据。
