# Function Tool Agent

## 一、项目目标

本项目在项目16的普通命令行LLM应用基础上，增加Function Tool和Agent Loop。
用户提出任务后，模型可以判断是否需要调用Python工具，程序执行工具，再把结果交给模型生成最终回答。

## 二、普通LLM与Function Tool Agent

普通LLM应用：

```text
用户 → LLM → 最终回答
```

Function Tool Agent：

```text
用户 → LLM → function_call → Python工具
                         ↓
                 function_call_output
                         ↓
                    LLM → 最终回答
```

模型不会直接执行Python函数。模型只会根据Tool Schema提出调用请求，真正的函数执行由Python程序控制。

## 三、项目结构

```text
17-项目02-FunctionToolAgent/
├── README.md
├── main.py
├── config.py
├── llm_client.py
├── tools.py
├── agent.py
├── requirements.txt
└── .env.example
```

- `main.py`：程序入口和命令行交互；
- `config.py`：读取API Key、模型和最大步数；
- `llm_client.py`：封装OpenAI Responses API请求；
- `tools.py`：定义安全工具、Tool Schema和工具白名单；
- `agent.py`：实现Agent Loop、参数解析和工具结果回传；
- `requirements.txt`：记录OpenAI SDK依赖；
- `.env.example`：展示环境变量名称。

## 四、Tool Calling完整流程

```text
1. Python把Tool Schema提供给模型
2. 模型返回function_call
3. Python读取name、arguments和call_id
4. Python通过白名单找到对应函数
5. Python解析参数并执行函数
6. Python生成function_call_output
7. 使用相同call_id把结果交给模型
8. 模型继续调用工具或生成最终回答
```

## 五、准备和运行

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
python main.py
```

Windows PowerShell可以使用：

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python main.py
```

输入`exit`或`quit`退出。

## 六、示例对话

```text
你：帮我计算123乘以456
Agent：调用calculate工具
Python：执行calculate(123, 456, "multiply")
Agent：把function_call_output交给模型
助手：结果是56088。
```

```text
你：告诉我我的学习进度
Agent：调用get_learning_record工具
Python：返回内存中的学习记录
助手：根据学习记录整理回答。
```

## 七、Agent Loop

`agent.py`使用有限循环：

```text
for step in range(MAX_STEPS):
    调用模型
    检查function_call
    执行所有已知工具
    返回工具结果
```

如果模型没有请求工具，就输出最终回答；如果达到最大步数，就停止循环并返回提示，避免无限运行。

## 八、本项目使用的Python知识

- 模块和`import`；
- 函数、参数和返回值；
- 列表、字典和集合；
- `for`循环和条件判断；
- JSON参数解析；
- `try / except`异常处理；
- 环境变量；
- 程序入口；
- 第三方SDK和HTTP API。

## 九、暂时没有涉及的内容

本项目不涉及LangChain、LangGraph、MCP、RAG、Memory框架、多Agent、数据库、Web UI、Shell工具、任意代码执行和大型工程框架。
