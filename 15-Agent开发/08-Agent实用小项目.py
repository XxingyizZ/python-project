# Agent实用小项目：学习助手Agent

# 项目目标：
# 用户提出学习任务 → LLM判断是否需要工具 → Python执行工具 → 返回工具结果 → 最终回答。

# 可提供的安全工具：
# 1. calculate：进行简单数学计算。
# 2. analyze_text：统计文本的字符数、单词数和数字数量。
# 3. get_learning_record：查询内存中的学习记录。

# learning_records = [
#     {"topic": "列表", "status": "已完成"},
#     {"topic": "函数", "status": "学习中"}
# ]

# def analyze_text(text):
#     digit_count = 0
#
#     for character in text:
#         if character.isdigit():
#             digit_count += 1
#
#     return {
#         "character_count": len(text),
#         "word_count": len(text.split()),
#         "digit_count": digit_count
#     }

# def get_learning_record(topic):
#     for record in learning_records:
#         if record["topic"] == topic:
#             return record
#     return {"topic": topic, "status": "没有记录"}

# Agent程序可以按照下面的结构组织：
# def call_model(...):
#     ...
#
# def run_agent(...):
#     for step in range(max_steps):
#         # 调用模型、检查function_call、执行白名单工具、回传结果
#         ...
#
# def main():
#     ...
#
# if __name__ == "__main__":
#     main()

# 这个项目综合使用了LLM、Tool、Function Tool、函数、数据容器、JSON、
# 异常处理、上下文和Agent Loop。
# 当前不学习MCP、RAG、Embedding、长期Memory、多Agent和大型Agent框架。
