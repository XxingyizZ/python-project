# 标准库综合使用
# 本章组合使用标准库、函数、字符串、列表、字典、集合、for和if。

# 案例1：使用re和Counter统计文本中的单词。
# import re
# from collections import Counter
#
# text = "Python is useful. Python is simple."
# words = re.findall(r"[A-Za-z]+", text.lower())
# word_counter = Counter(words)
# print(word_counter)

# 案例2：使用datetime处理带日期的数据。
# from datetime import datetime, timedelta
#
# records = [
#     {"date": "2026-01-01", "content": "学习Python"},
#     {"date": "2026-01-03", "content": "练习函数"}
# ]
# start_date = datetime.strptime("2026-01-02", "%Y-%m-%d")
# for record in records:
#     record_date = datetime.strptime(record["date"], "%Y-%m-%d")
#     if record_date >= start_date:
#         print(record["content"])

# 案例3：使用pathlib整理路径信息。
# from pathlib import Path
#
# paths = [Path("data.txt"), Path("student.json"), Path("notes")]
# path_info = []
# for path in paths:
#     path_info.append({
#         "name": path.name,
#         "suffix": path.suffix,
#         "is_file": path.is_file(),
#         "is_dir": path.is_dir()
#     })
# print(path_info)

# 标准库可以和前面学习的函数、数据容器组合使用，完成实际的数据处理任务。
# 当前案例只检查示例路径，不主动扫描或修改用户目录。
