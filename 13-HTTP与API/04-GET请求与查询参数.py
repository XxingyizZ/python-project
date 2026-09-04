# GET请求与查询参数

# GET通常用于从服务器获取数据。

# 可以使用params参数传递查询参数，不需要手动拼接复杂URL。
# import requests
#
# response = requests.get(
#     "https://httpbin.org/get",
#     params={"name": "Tom", "age": 18}
# )
# print(response.url)
# print(response.status_code)
# print(response.json())

# params字典中的数据会被转换为URL查询参数。
# 例如可能得到类似：
# https://httpbin.org/get?name=Tom&age=18

# headers可以传递请求头：
# headers = {"Accept": "application/json"}
# response = requests.get(
#     "https://httpbin.org/get",
#     params={"keyword": "python"},
#     headers=headers
# )
# print(response.json())

# 当前只学习基础GET、params和headers，不展开HTTP标准细节。
