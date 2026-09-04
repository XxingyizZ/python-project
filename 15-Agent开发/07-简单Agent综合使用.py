# 简单Agent综合使用

# 案例一：计算Agent。
# 可以提供add、subtract和multiply等纯数学工具。
# 用户提出计算任务，LLM请求工具，Python执行函数并返回结果。

# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b

# 案例二：多工具Agent。
# 除计算器外，再提供文本统计工具：
# def text_length(text):
#     return len(text)
#
# Agent可以先调用multiply，再调用text_length处理上一步结果。

# 案例三：信息整理Agent。
# 使用内存中的示例数据查询学生成绩：
# students = {
#     "小明": {"score": 85},
#     "小红": {"score": 92}
# }
#
# def get_student_score(name):
#     if name not in students:
#         return "没有找到这个学生"
#     return students[name]["score"]

# 这些案例逐步综合：
# 一个工具 → 多个工具 → 工具与列表、字典和条件判断组合。
# 当前不访问真实文件、数据库或外部服务。
