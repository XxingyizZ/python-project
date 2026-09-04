# LLM学习笔记

LLM可以根据Prompt生成文本结果。
Python程序可以通过Responses API调用LLM，并读取模型返回的内容。

多轮上下文需要保留之前的对话信息，或者使用API提供的上下文标识继续对话。
结构化输出可以让模型结果更容易转换成JSON和Python字典。
