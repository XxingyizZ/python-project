# 文件工具Agent

## 一、项目目标

本项目让Agent通过安全、明确的Function Tool读取和搜索项目内部的少量学习笔记。
它把Agent、Function Tool、Python文件操作、工具结果和LLM连接起来，为后续RAG学习打基础。

本项目不是RAG，也不允许Agent任意访问电脑文件。

## 二、Agent如何访问学习笔记

```text
用户 → LLM → function_call → Python文件工具
                         ↓
                 function_call_output
                         ↓
                    LLM → 最终回答
```

程序只提供`list_notes()`、`read_note(name)`和`search_notes(keyword)`三个工具。
工具内部把文件访问限制在本项目的`data/notes/`目录中。

## 三、项目结构

```text
18-项目03-文件工具Agent/
├── README.md
├── main.py
├── config.py
├── llm_client.py
├── tools.py
├── agent.py
├── requirements.txt
├── .env.example
└── data/
    └── notes/
        ├── python.md
        ├── llm.md
        └── agent.md
```

- `main.py`：命令行入口；
- `config.py`：API Key、模型和最大步数；
- `llm_client.py`：调用OpenAI Responses API；
- `tools.py`：文件工具、Tool Schema和工具白名单；
- `agent.py`：处理function_call并运行Agent Loop；
- `data/notes/`：项目自带的测试笔记数据。

## 四、安装和运行

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

## 五、示例对话

```text
你：Python函数的笔记在哪里？
Agent：调用search_notes工具搜索“函数”。
Python：读取data/notes/中的允许文件。
Agent：把工具结果交给模型。
助手：根据搜索到的内容回答。
```

## 六、这个项目为什么还不是RAG？

本项目沿用Project 17的Agent Loop，本项目新增的是受限文件Tool。

当前项目是：

```text
Agent → search_notes() → Python字符串搜索 → 返回结果
```

RAG通常是：

```text
文档集合 → 文档切分 → Embedding → 向量检索 → 找到相关内容 → LLM
```

文件Tool解决的是“让Agent能够访问指定数据”。
RAG解决的是“让系统能够从大量数据中检索相关内容”。两者不是同一个概念。
Project 19会在这个文件搜索基础上继续学习文档切分、Embedding和相似度检索。

## 七、安全边界

- 只能访问`data/notes/`中的指定Markdown文件；
- 工具参数是笔记名称或搜索关键词，不接受任意路径；
- 不允许绝对路径和`../`路径穿越；
- 不写入、不删除项目文件；
- 不执行Shell、Python代码或数据库操作；
- Agent有最大执行步数；
- 不在代码中保存真实API Key。

## 八、项目使用的Python知识

本项目综合使用了`pathlib`、文件读取、函数、列表、字典、JSON、异常处理、环境变量、模块、`for`、`if`和程序入口。
