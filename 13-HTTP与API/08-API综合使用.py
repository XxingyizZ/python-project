# API综合使用

# 案例一：GET + params + JSON + 字典
# import requests
#
# response = requests.get(
#     "https://httpbin.org/get",
#     params={"keyword": "python"},
#     timeout=5
# )
# response.raise_for_status()
# result = response.json()
# print(result["args"])

# 案例二：POST + JSON + 异常处理
# import requests
#
# student = {"name": "小明", "score": 85}
#
# try:
#     response = requests.post(
#         "https://httpbin.org/post",
#         json=student,
#         timeout=5
#     )
#     response.raise_for_status()
#     result = response.json()
#     print(result["json"])
# except requests.RequestException as e:
#     print("请求失败：", e)

# 案例三：请求、检查、解析、处理、输出
# import requests
#
# try:
#     response = requests.get("https://httpbin.org/json", timeout=5)
#     response.raise_for_status()
#     data = response.json()
#
#     slides = data.get("slideshow", {}).get("slides", [])
#     for slide in slides:
#         if "title" in slide:
#             print(f"标题：{slide['title']}")
# except requests.RequestException as e:
#     print("请求失败：", e)

# API程序的基本流程：
# 请求API → 检查状态 → 解析JSON → 取得数据 → for/if处理 → 输出结果
