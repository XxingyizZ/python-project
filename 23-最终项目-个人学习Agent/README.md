# 23-最终项目：个人学习 Agent

这是 Python → LLM → Agent 学习路线的最终综合项目：一个可以对话、查询学习知识、记住有限用户信息并执行安全计算的个人学习助手。

## 一、完整架构

```text
用户 → main.py → Agent
                  ├── LLM
                  ├── Memory(JSON)
                  ├── RAG Tool → 知识库
                  ├── Function Tools → Python函数
                  └── MCP Client(可选) → MCP Server → 外部Tool
                         ↓
                    Tool Result → LLM → 最终回答
```

LLM 负责理解和生成，Agent 负责协调和决策，Tool 负责执行动作，RAG 负责检索知识，Memory 负责保存状态，MCP 负责标准化连接外部工具和资源。

## 二、项目结构

```text
23-最终项目-个人学习Agent/
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
├── mcp_client.py
├── mcp_server.py
├── requirements.txt
├── .env.example
└── data/
    ├── memory.json
    └── knowledge/
        ├── python.md
        ├── llm.md
        ├── agent.md
        └── mcp.md
```

## 三、运行

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key_here"
python main.py
```

输入 `exit` 或 `quit` 退出。示例问题：

```text
我叫小明。
我叫什么？
什么是 Agent Loop？
帮我计算 123 * 456。
我叫什么？另外解释一下 Agent Loop。
```

## 四、Agent Loop

```text
用户问题 → Memory Context → Responses API
→ 检查 response.output → function_call？
→ 本地 Tool 或 MCP Tool → function_call_output(call_id)
→ 再次请求模型 → 最终回答
```

一个响应可能包含多个工具调用，程序会逐个执行并把多个结果一起返回。Tool Schema 描述 Python 工具的名称、用途和参数；模型产生 `function_call`，Python 根据白名单执行，再用对应的 `call_id` 发送 `function_call_output`。

## 五、Memory 和 RAG

Memory 保存用户长期状态（姓名、学习目标）和有限的对话历史；RAG 读取 `data/knowledge/`，切分文档、生成 Embedding、计算余弦相似度并返回 Top-K 的 `source/text/score`。Memory 不等于 RAG，`previous_response_id` 也不等于持久化 Memory。

RAG 被注册为 Tool，Agent 需要知识时调用 `search_knowledge`，而不是让 Agent 偷偷直接访问 RAG 模块。

## 六、MCP 可选扩展

Function Tool 直接注册在当前 Agent 中；MCP Tool 由 MCP Server 提供，MCP Client 负责连接和发现。安装可选依赖后，可设置 `ENABLE_MCP=true`，让 Agent 尝试连接本项目的本地 MCP Server，发现并调用 `list_notes`、`read_note`。如果没有 MCP SDK，核心本地 Tool、Memory 和 RAG 仍可正常加载。

```bash
pip install "mcp[cli]"
export ENABLE_MCP=true
```

MCP 不等于 Agent；本项目也不把 MCP 强行作为核心依赖。

## 七、为什么这样设计

- Agent Loop 让模型可以在回答前执行动作；`MAX_STEPS` 防止循环无限执行；
- Tool 白名单和参数校验防止模型字符串变成任意代码；
- RAG 适合补充指定文档，Memory 适合保存用户状态；
- `source` 让检索结果可追溯；
- 只把简短 Memory Context 和有限历史提供给模型，避免上下文无限增长。

## 八、安全边界与限制

这是学习项目，不是生产级 Agent。没有数据库、向量数据库、Web、Docker、复杂权限、分布式架构或高级评估系统。禁止 `eval`、`exec`、Shell、任意路径访问、删除文件、网络扫描和保存 API Key。Memory 只能更新 `name` 与 `learning_goal`，知识库和 Memory 路径固定在项目 `data/` 中。
