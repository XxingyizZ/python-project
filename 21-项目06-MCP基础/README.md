# 21-项目06：MCP 基础

## 一、项目目标

本项目使用官方 MCP Python SDK，创建一个最小的 MCP Server 和 MCP Client。
重点理解：一个程序如何通过 MCP 发现并调用另一个程序提供的工具。

本项目暂时不是 Agent，也不负责调用大语言模型。它先把 MCP 的基本通信关系学清楚。

## 二、项目功能

Server 提供三个安全工具：

- `calculate`：执行限定的加、减、乘、除；
- `list_notes`：列出项目内允许读取的学习笔记；
- `read_note`：读取白名单中的学习笔记。

Client 会启动本地 Server，通过 stdio 建立 MCP 连接，然后：

1. 初始化 MCP 会话；
2. 使用 `list_tools()` 发现工具名称、说明和输入结构；
3. 使用 `call_tool()` 调用示例工具；
4. 在退出上下文时关闭连接和 Server 子进程。

## 三、MCP 的基本角色

```text
Host
└── Client ── MCP 协议 ── Server
                           └── Tools / Resources / Prompts
```

- Host：使用 MCP 的宿主应用，可以包含用户界面和一个或多个 Client；
- Client：负责连接 Server、发现能力、发送调用请求；
- Server：负责提供工具、资源或提示；
- Tool：可以被调用的动作，例如这里的计算和读取笔记；
- Resource：由 Server 提供的上下文资源，例如文档内容。本项目只介绍概念，暂不实现 Resource。

一次调用的基本流程是：

```text
Client 启动 Server
→ 初始化会话
→ list_tools() 发现工具
→ call_tool() 调用工具
→ Server 执行安全函数
→ Client 接收结果
```

## 四、MCP 与前面知识的关系

- Function Tool：通常是某个 LLM 应用内部声明和执行函数；
- MCP：规定 Client 与独立 Server 如何发现和调用工具，工具可以被不同的 Host 使用；
- Agent：通常还包含模型、任务循环和决策过程，本项目没有加入；
- RAG：关注检索资料并提供上下文，本项目只提供一个受限的笔记读取工具，不是 RAG 系统。

## 五、目录结构

```text
21-项目06-MCP基础/
├── README.md
├── client.py
├── server.py
├── tools.py
├── config.py
├── main.py
├── requirements.txt
├── .env.example
└── data/notes/
    ├── python.md
    ├── agent.md
    └── mcp.md
```

## 六、准备环境

建议使用 Python 3.10 或更高版本，并在项目外层创建虚拟环境：

```bash
python3 -m venv .venv
source .venv/bin/activate
```

安装本项目真正使用的依赖：

```bash
pip install -r requirements.txt
```

本项目不需要 OpenAI API Key，也不调用 OpenAI API。`.env.example` 中的路径配置是可选的。

## 七、运行项目

在项目目录中运行：

```bash
python main.py
```

程序会自动以 stdio 子进程方式启动 `server.py`，并完成工具发现与调用示例。stdio 的标准输出属于 MCP 通信通道，因此 Server 不应该随意向 stdout 打印调试信息。

预期会看到类似结果：

```text
已发现工具：calculate, list_notes, read_note
计算结果：30
笔记列表：...
```

## 八、文件职责

- `config.py`：集中确定 Server 路径和 Python 解释器；
- `tools.py`：保存独立、安全的本地工具函数；
- `server.py`：使用 MCP SDK 注册并运行工具；
- `client.py`：通过 stdio 连接 Server、发现并调用工具；
- `main.py`：程序入口；
- `data/notes/`：供受限读取的示例资料。

## 九、安全边界

- 计算只允许四种明确运算，不使用 `eval()`、`exec()` 或 Shell；
- 笔记只能从白名单文件中读取；
- 不接受绝对路径和路径穿越写法；
- 不写入、不删除文件；
- 不访问网络，不执行任意 Python 代码。

## 十、本项目暂时没有涉及什么

本项目没有加入 LLM、Agent、Function Calling、MCP Resource 的实际实现、MCP Prompt、数据库、网络 HTTP、RAG、Memory、Web UI 或大型框架。这些内容可以在掌握 MCP 基本通信后再学习。

## 十一、继续学习

官方 MCP Python SDK 当前稳定文档是 v2。后续可以在理解本项目的 Client、Server、Tool、stdio 之后，再学习如何把 MCP 接入模型或 Agent。
