# 22-项目07：Agent + RAG + Memory 综合项目

## 一、项目目标

本项目把前面学过的 LLM、Function Tool、Agent Loop、RAG、Memory、JSON 和文件操作组合起来，完成一个可以运行的学习助手。
它不是重新学习这些概念，而是组合 Project 17、19 和 20 已经建立的机制。

```text
用户问题
  ↓
Agent
  ├── Memory：保存用户状态
  ├── RAG Tool：检索知识库
  └── Function Tool：执行计算
          ↓
      Python 工具结果
          ↓
        LLM
          ↓
       最终回答
```

## 二、几个东西分别负责什么

| 内容 | 负责的事情 |
| --- | --- |
| LLM | 理解问题、决定是否需要工具、生成回答 |
| Agent | 组织循环，决定下一步动作 |
| Tool | 执行明确的动作，例如计算或更新 Memory |
| RAG | 从指定知识库检索相关内容 |
| Memory | 保存应用自己的状态，例如姓名和学习目标 |
| MCP | 标准化连接外部 Tool/Resource，本项目暂不集成 |

普通 LLM 只接收问题并生成回答；Agent 可以先调用一个或多个工具，再把工具结果交给模型继续回答。

## 三、项目功能

- 普通问题交给 Responses API 回答；
- `calculate` 执行安全的四则运算；
- `search_knowledge` 通过 Embedding、余弦相似度和 Top-K 检索知识库；
- `get_memory` 和 `update_memory` 读取或更新有限的用户信息；
- 保存最近的对话和用户状态到 `data/memory.json`；
- 一个请求可以包含多个 `function_call`；
- 工具结果通过 `function_call_output` 和 `call_id` 返回模型。

## 四、目录结构

```text
22-项目07-Agent+RAG+Memory综合项目/
├── README.md
├── main.py
├── config.py
├── agent.py
├── llm_client.py
├── tools.py
├── memory.py
├── documents.py
├── embeddings.py
├── retriever.py
├── rag.py
├── requirements.txt
├── .env.example
└── data/
    ├── memory.json
    ├── index.json
    └── knowledge/
        ├── python.md
        ├── llm.md
        └── agent.md
```

## 五、运行流程

```text
用户输入
→ Agent 构建简短 Memory Context
→ Responses API
→ 检查 response.output
→ 发现 function_call
→ 白名单查找工具
→ Python 执行工具
→ function_call_output（带 call_id）
→ 再次调用模型
→ 最终回答
```

`search_knowledge` 是一个 Agent Tool，所以 Agent 不会偷偷直接调用 RAG。RAG 先检索包含 `source`、`text`、`score` 的结果，再作为工具结果提供给模型。

## 六、安装和配置

建议使用 Python 3.10 或更高版本：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

复制 `.env.example` 中的配置，并设置真实的 `OPENAI_API_KEY`。不要把真实密钥写进代码或提交到仓库。

```bash
export OPENAI_API_KEY="your_api_key_here"
python main.py
```

Windows PowerShell：

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
python main.py
```

首次需要 RAG 检索时，如果 `data/index.json` 不存在或文档内容发生变化，程序会调用 Embeddings API 建立索引，因此也需要 API Key。

## 七、示例问题

```text
什么是 Agent Loop？
我叫小明。
我叫什么？我现在学习什么？
帮我计算 123 * 456。
解释 Agent Loop，并顺便计算 123 * 456。
```

本项目不会保证模型每次都选择完全相同的工具。工具说明和用户问题会影响模型决定，但 Python 端始终通过工具白名单限制可执行内容。

## 八、Memory、RAG 和 previous_response_id 的区别

- Memory 是应用主动保存的持久化状态，写在 `memory.json` 中；
- RAG 是应用根据问题检索知识，并把相关内容放进当前上下文；
- `previous_response_id` 只是把连续的 Responses 请求关联起来，不等于应用自己的 Memory；
- Tool 是一次可控的动作，不等于 Memory 或 RAG。

程序只向模型提供简短的 Memory Context，不会把整个 `memory.json` 原样塞进每次请求。对话历史、Top-K 结果和 chunk 长度也都有上限。

## 九、限制和安全边界

- 不使用 LangChain、LangGraph、向量数据库、数据库或 Web 框架；
- 不使用 `eval()`、`exec()`、Shell 或任意 Python 执行；
- 只能读取 `data/knowledge/` 下固定的知识文档；
- Memory 只能修改 `name` 和 `learning_goal`；
- 不保存 API Key、Token、密码、身份证号或信用卡信息；
- 不处理任意路径，不删除文件，不访问网络扫描目标；
- 不使用列表推导式、复杂 Agent 框架或多 Agent 设计。

## 十、下一步

完成本项目后，可以进入最终项目，把这些基础能力放入更接近实际使用的应用中，并在需要时学习 MCP、异步或更完整的工程部署方式。
