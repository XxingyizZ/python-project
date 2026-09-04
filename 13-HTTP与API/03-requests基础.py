# requests基础

# requests是Python中常用的HTTP请求库。
# 它是第三方库，需要先安装：
# python -m pip install requests

# 使用requests前需要导入：
# import requests

# 最简单的GET请求：
# response = requests.get("https://httpbin.org/get")
# print(response.status_code)
# print(response.text)

# Response对象保存服务器返回的响应。
# response.status_code → HTTP状态码
# response.text        → 响应文本
# response.json()      → 将JSON响应解析为Python数据

# JSON响应解析示例：
# import requests
# response = requests.get("https://httpbin.org/get")
# result = response.json()
# print(result)

# 本章的requests示例使用公开测试地址，只作为学习示意。
# 不在当前项目中自动安装第三方库。
