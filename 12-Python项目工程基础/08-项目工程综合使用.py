# 项目工程综合使用

# 一个简单的学生项目可以有下面的结构：
# student_project/
# ├── main.py
# ├── utils.py
# ├── requirements.txt
# ├── .gitignore
# └── .venv/

# main.py       → 程序入口，负责启动程序。
# utils.py      → 功能模块，负责提供可复用的功能。
# .venv/        → 项目的相对独立运行环境。
# requirements.txt → 项目依赖记录。
# .gitignore    → 忽略不应该提交的文件。

# 假设utils.py中提供一个读取学生姓名的函数：
# def get_student_name(student):
#     return student["name"]

# main.py导入并使用这个功能：
# import os
# import utils
#
# def main():
#     program_name = os.getenv("PROGRAM_NAME", "学生成绩程序")
#     student = {"name": "小明", "score": 85}
#     print(program_name)
#     print(utils.get_student_name(student))
#
# if __name__ == "__main__":
#     main()

# 这些工程概念共同组成项目的基本骨架：
# main.py         → 入口
# utils.py        → 模块
# .venv/          → 环境
# requirements.txt → 依赖
# 环境变量        → 配置
# .gitignore      → 文件管理规则

# 本示例只做结构说明，不要求真的创建完整项目。
