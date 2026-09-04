# 实用小项目：文本数据统计与分析工具
# 本项目使用re、Counter、datetime、函数、列表、字典、集合、for和if。

# import re
# from collections import Counter
# from datetime import datetime

# 使用函数提取文本中的单词。
# def get_words(text):
#     return re.findall(r"[A-Za-z]+", text.lower())

# 使用函数统计文本中的单词。
# def count_words(words):
#     return Counter(words)

# 使用函数统计文本中的数字。
# def get_numbers(text):
#     return re.findall(r"\d+", text)

# 使用函数组织分析结果。
# def analyze_text(text):
#     words = get_words(text)
#     word_counter = count_words(words)
#     numbers = get_numbers(text)
#     result = {
#         "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "character_count": len(text),
#         "word_count": len(words),
#         "number_count": len(numbers),
#         "most_common_words": word_counter.most_common(3),
#         "unique_words": set(words)
#     }
#     return result

# text = "Python is useful. Python is simple. Version 3 is popular."
# result = analyze_text(text)
# print("分析时间：", result["time"])
# print("字符数量：", result["character_count"])
# print("单词数量：", result["word_count"])
# print("数字数量：", result["number_count"])
# print("高频单词：", result["most_common_words"])
# print("不重复单词数量：", len(result["unique_words"]))

# 数据流程：文本 → re提取 → Counter统计 → 字典组织结果 → 输出。
# 如果以后需要分析文件，可以再结合前面学习过的文件操作和异常处理。
# 本章不引入第三方库、日志框架或复杂项目结构。
