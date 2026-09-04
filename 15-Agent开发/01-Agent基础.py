# Agent基础

# 第14章的普通LLM应用通常是：
# 用户输入 → LLM → 模型输出

# Agent是一种让LLM根据目标进行判断、选择行动、调用工具，
# 并根据工具结果继续执行的程序系统。

# Agent的基本流程：
# 用户任务 → LLM → 决定行动 → 工具 → 工具结果 → LLM → 继续或结束

# Agent通常由下面几部分组成：
# LLM          → 理解任务并决定下一步
# Instructions → 提供行为指引
# Tools        → 提供外部能力
# Context      → 保存当前任务所需的信息
# 执行循环     → 反复调用模型和工具

# Agent不等于某一个特殊模型名称。
# Agent更多是一种应用程序的组织方式。

# 本章使用基础Python和OpenAI Responses API理解Agent机制。
# 当前不学习MCP、RAG、长期Memory、多Agent或大型Agent框架。
