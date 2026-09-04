# HTTP状态码与异常处理

# 常见状态码：
# 200 OK                    → 请求成功
# 201 Created               → 创建资源成功
# 400 Bad Request           → 请求内容有问题
# 401 Unauthorized         → 未通过身份认证
# 403 Forbidden            → 没有访问权限
# 404 Not Found             → 请求的资源不存在
# 500 Internal Server Error → 服务器内部错误

# 状态码的基本分类：
# 2xx → 成功
# 3xx → 重定向
# 4xx → 客户端请求问题
# 5xx → 服务器问题

# raise_for_status()可以检查HTTP错误状态。
# 成功响应通常不会抛出HTTPError，失败状态可能抛出异常。
# import requests
#
# try:
#     response = requests.get("https://httpbin.org/status/404", timeout=5)
#     response.raise_for_status()
# except requests.RequestException as e:
#     print("请求失败：", e)

# 网络请求可能因为网络、服务器或请求内容等原因失败。
# 因此API程序通常需要使用try/except处理请求异常。

# timeout用于限制等待响应的时间，避免程序无限等待。
# response = requests.get("https://httpbin.org/get", timeout=5)
