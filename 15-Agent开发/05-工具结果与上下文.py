# 工具结果与上下文

# LLM请求调用add(1, 2)后，Python执行函数得到3。
# 模型必须知道“工具结果是3”，才能继续回答。

# Responses API中，可以保存模型输出，并把工具结果追加到输入中：
# input_list += response.output
# input_list.append({
#     "type": "function_call_output",
#     "call_id": tool_call.call_id,
#     "output": "3"
# })

# call_id用于把工具结果对应到模型发出的那一次调用。
# 工具结果通常需要转换为字符串或JSON字符串后再回传。

# 多个工具可以连续调用：
# 用户：计算10乘20，并说明结果有多少位。
# LLM → multiply(10, 20) → 200
# LLM → text_length("200") → 3
# LLM → 最终回答

# 当前任务的上下文可以包含：
# 用户任务、模型输出、工具调用和工具结果。
# 这些信息共同帮助模型继续判断。

# 本章只讲当前任务执行过程中的上下文，不讲长期记忆、向量数据库和RAG。
