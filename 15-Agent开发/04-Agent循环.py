# Agent循环

# Agent的核心不是只调用一次工具，而是：
# 调用工具 → 得到结果 → 再让模型决定下一步。

# 基本流程：
# 用户任务 → 调用LLM
# 如果是最终文本 → 结束
# 如果是function_call → 执行工具 → 回传结果 → 再调用LLM

# 下面是简化的Agent循环结构：
# import json
# from openai import OpenAI
#
# client = OpenAI()
# input_list = [{"role": "user", "content": "请计算123加456。"}]
# max_steps = 5
#
# for step in range(max_steps):
#     response = client.responses.create(
#         model="gpt-5.6",
#         tools=tools,
#         input=input_list
#     )
#     input_list += response.output
#
#     tool_was_called = False
#     for item in response.output:
#         if item.type != "function_call":
#             continue
#
#         tool_was_called = True
#         arguments = json.loads(item.arguments)
#         result = add(arguments["a"], arguments["b"])
#         input_list.append({
#             "type": "function_call_output",
#             "call_id": item.call_id,
#             "output": str(result)
#         })
#
#     if not tool_was_called:
#         print(response.output_text)
#         break

# 最大循环次数可以防止Agent无限运行。
# 其他终止条件还包括工具失败、异常或用户取消任务。
# 当前只展示正常完成和最大步数两种基本情况。
