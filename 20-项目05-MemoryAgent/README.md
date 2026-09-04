# Memory Agent

## 一、项目目标

本项目实现一个最小的Memory Agent，让程序保存、读取和使用用户过去的信息。
例如用户说“我叫小明”，程序把姓名保存到`data/memory.json`；程序重启后仍然可以读取这条信息。

LLM本身不会因为Python程序结束而自动永久记住用户信息，持久化Memory需要由应用程序设计和保存。

## 二、Memory的几种形式

- 短期记忆：当前任务中暂时使用的信息，例如上一句话；
- 对话历史：最近几轮用户和助手的对话；
- 长期记忆：相对稳定的用户事实，例如姓名和学习目标；
- 持久化记忆：保存到JSON文件，程序重启后仍然存在。

## 三、项目结构

```text
20-项目05-MemoryAgent/
├── README.md
├── main.py
├── config.py
├── llm_client.py
├── memory.py
├── agent.py
├── requirements.txt
├── .env.example
└── data/
    └── memory.json
```

- `memory.py`：读取、保存和更新Memory；
- `agent.py`：构建Memory Context、执行Memory Tool和Agent Loop；
- `llm_client.py`：调用OpenAI Responses API；
- `main.py`：命令行入口；
- `data/memory.json`：教学用持久化Memory。

## 四、Memory与对话历史

对话历史记录“最近谈过什么”，例如“刚才讨论了Python函数”。
长期记忆记录“用户的稳定事实”，例如“用户叫小明”。本项目只保存最近有限条对话，避免上下文无限增长。

## 五、Memory与RAG的区别

RAG主要从知识库中检索外部知识，例如查找“Python列表是什么”。
Memory主要保存用户或Agent的历史状态，例如记住“用户叫小明”。两者解决的是不同问题。

## 六、Memory与previous_response_id的区别

`previous_response_id`用于连接连续的Responses API上下文；Memory是应用自己保存的JSON数据。
两者可以同时使用，但`previous_response_id`不是永久记忆，JSON Memory也不等于API服务端的对话上下文。

## 七、安装和运行

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
python main.py
```

Windows PowerShell：

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python main.py
```

输入`exit`或`quit`退出。

## 八、Agent流程

```text
用户输入 → 读取Memory → LLM → function_call？
                              ↓
                 Python执行Memory Tool
                              ↓
                 function_call_output → LLM
                              ↓
                         最终回答
```

程序会把适合当前问题的Memory整理成简单上下文后提供给模型，而不是把整个JSON文件无条件塞给模型。

## 九、安全和隐私

Memory文件只保存教学用的姓名、学习目标和对话示例，不保存API Key、密码、Token、信用卡或身份证号。
真实项目还需要考虑用户授权、隐私保护、数据删除和访问控制。
