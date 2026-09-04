# POST请求与JSON数据

# POST通常用于向服务器提交数据。

# 使用json参数提交Python字典时，requests会按照JSON请求数据发送。
# import requests
#
# data = {
#     "name": "Tom",
#     "age": 18
# }
#
# response = requests.post(
#     "https://httpbin.org/post",
#     json=data,
#     timeout=5
# )
# print(response.status_code)
# print(response.json())

# 数据流程：
# Python字典 → requests → JSON请求数据 → 服务器

# json=data和data=data不是完全相同的写法。
# 本章传递JSON对象时优先使用json=参数。
# 当前不学习multipart/form-data等其他请求数据格式。

# response.json()可以将JSON响应转换为Python字典或列表。
