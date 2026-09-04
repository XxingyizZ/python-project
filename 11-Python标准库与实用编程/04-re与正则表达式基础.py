# re与正则表达式基础
# 正则表达式是一种描述文本匹配规则的方式。
# import re

# re.search()会在字符串中寻找符合规则的内容。
# 找到时返回匹配对象，找不到时返回None。
# text = "学习Python很有趣"
# result = re.search(r"Python", text)
# if result:
#     print(result.group())

# re.match()从字符串开头进行匹配。
# print(re.match(r"Python", "Python学习"))
# print(re.match(r"Python", "学习Python"))

# re.findall()可以找到所有符合规则的内容，并返回一个列表。
# text = "Python 123 Java 456"
# numbers = re.findall(r"\d+", text)
# print(numbers)

# 常见正则符号：
# \d表示数字，\w表示字母、数字或下划线，\s表示空白字符。
# .表示任意单个字符，+表示前面的规则出现一次或多次，
# *表示前面的规则出现零次或多次，?表示出现零次或一次。
# []表示匹配方括号中的任意一个字符，^表示开头，$表示结尾。

# text = "编号：A123，数量：45"
# print(re.findall(r"\d+", text))
# print(re.findall(r"[A-Z]\d+", text))

# r"\d+"中的r表示原始字符串，可以减少反斜杠转义带来的干扰。
# 正则表达式规则复杂时，应优先保证代码能够读懂。
