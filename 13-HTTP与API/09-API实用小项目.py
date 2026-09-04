# API实用小项目：API数据查询工具

# 本案例展示一个简单的项目结构，不连接需要注册或密钥的业务API。
# 项目目标：输入查询条件，调用测试API，读取并输出返回数据。

# import requests
#
# def fetch_data(keyword):
#     response = requests.get(
#         "https://httpbin.org/get",
#         params={"keyword": keyword},
#         timeout=5
#     )
#     response.raise_for_status()
#     return response.json()
#
# def process_data(data):
#     query_data = data.get("args", {})
#
#     for key, value in query_data.items():
#         print(f"{key}：{value}")
#
# def main():
#     keyword = input("请输入查询内容：")
#
#     try:
#         data = fetch_data(keyword)
#         process_data(data)
#     except requests.RequestException as e:
#         print("API请求失败：", e)
#
# if __name__ == "__main__":
#     main()

# 这个小项目使用了：
# requests、函数、字典、for、异常处理、JSON数据和程序入口。
# input()案例需要用户输入，因此只进行静态检查，不自动运行。

# 不要在真实项目中把API Key、Token、密码或Cookie直接写入代码。
# 当前不学习LLM API、Agent、MCP、数据库和Web框架。
