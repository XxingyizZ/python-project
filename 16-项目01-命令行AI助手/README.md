# 命令行AI助手

## 一、项目目标

本项目使用Python编写一个可以在命令行中运行的AI助手。
它会读取用户输入，调用OpenAI Responses API，并把模型回答输出到终端。

本项目是一个普通的LLM应用，还不是Agent。

## 二、项目功能

- 在命令行中获取用户输入；
- 调用OpenAI模型生成回答；
- 支持连续多轮对话；
- 通过环境变量读取API Key和模型配置；
- 处理API Key缺失、API调用失败和用户退出。

## 三、项目结构

```text
16-项目01-命令行AI助手/
├── README.md
├── main.py
├── config.py
├── llm_client.py
├── chat.py
├── requirements.txt
└── .env.example
```

- `main.py`：程序入口；
- `config.py`：读取和管理配置；
- `llm_client.py`：封装LLM API调用；
- `chat.py`：处理命令行多轮聊天；
- `requirements.txt`：记录项目直接依赖；
- `.env.example`：展示环境变量配置名称，不包含真实密钥。

## 四、运行流程

```text
用户输入
    ↓
Python命令行程序
    ↓
OpenAI Responses API
    ↓
模型回答
    ↓
Python程序
    ↓
用户
```

多轮聊天时，程序保存上一轮响应的ID，并通过`previous_response_id`告诉API继续当前对话。

## 五、准备虚拟环境

在项目目录中创建虚拟环境：

```bash
python -m venv .venv
```

macOS或Linux激活：

```bash
source .venv/bin/activate
```

Windows激活：

```bash
.venv\Scripts\activate
```

## 六、安装依赖

```bash
python -m pip install -r requirements.txt
```

本项目只直接依赖OpenAI官方Python SDK。

## 七、配置API Key

复制`.env.example`中的配置说明，并在当前终端设置环境变量。

macOS或Linux：

```bash
export OPENAI_API_KEY="your_api_key_here"
```

Windows PowerShell：

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

也可以设置可选的模型名称：

```bash
export OPENAI_MODEL="gpt-5.6"
```

不要把真实API Key写入Python文件、`.env.example`或Git仓库。

## 八、运行项目

```bash
python main.py
```

输入`exit`或`quit`可以退出程序。

## 九、使用示例

```text
你：你好
助手：你好！有什么可以帮助你？
你：我叫小明。
助手：很高兴认识你，小明。
你：我叫什么？
助手：你叫小明。
你：exit
程序结束。
```

实际回答由模型生成，示例只用于说明交互形式。

## 十、本项目涉及的Python知识

- 模块与`import`；
- 函数、参数和返回值；
- 环境变量；
- 字符串和变量；
- `while`循环和条件判断；
- `try / except`异常处理；
- 程序入口`if __name__ == "__main__"`；
- 第三方库和API调用。

## 十一、本项目暂时没有涉及

本项目暂时不涉及Agent、Function Calling、Tool Calling、MCP、RAG、Memory、数据库、Web界面、异步编程和大型框架。

当前重点是理解：Python程序如何调用LLM API并形成一个可运行的小项目。
