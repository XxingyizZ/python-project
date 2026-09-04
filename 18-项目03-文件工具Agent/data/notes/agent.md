# Agent学习笔记

Agent可以根据用户任务判断是否需要调用Tool。
Function Calling的基本流程是：模型提出function_call，Python执行工具，再返回function_call_output。

Agent Loop会重复调用模型和工具，直到模型生成最终回答或达到最大执行步数。
工具应该使用明确的白名单，并验证模型提供的参数。
