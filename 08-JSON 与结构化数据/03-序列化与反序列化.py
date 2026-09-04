# 序列化与反序列化
# 序列化：把Python对象转换成JSON字符串。
# 反序列化：把JSON字符串转换成Python对象。

# json.dumps()将Python对象转换成JSON字符串。
# import json
# student = {
#     "name": "小明",
#     "age": 18,
#     "score": 90
# }
# json_text = json.dumps(student, ensure_ascii=False)
# print(json_text)

# json.loads()将JSON字符串转换成Python对象。
# import json
# json_text = '{"name": "小明", "age": 18}'
# student = json.loads(json_text)
# print(student)
# print(student["name"])

# dumps和loads处理的是JSON字符串。
# dumps：Python对象 → JSON字符串
# loads：JSON字符串 → Python对象

# JSON字符串中的true、false和null转换到Python后，分别对应True、False和None。
# import json
# json_text = '{"passed": true, "remark": null}'
# data = json.loads(json_text)
# print(data)
