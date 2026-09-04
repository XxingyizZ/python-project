# RAG基础

## 一、项目目标

本项目不依赖RAG框架，使用Python、OpenAI Embeddings API和Responses API实现一个最小RAG流程：

```text
文档 → 文本切分 → Embedding → 保存向量
问题 → 问题Embedding → 余弦相似度 → Top-K检索
检索结果 → 上下文 → LLM → 回答
```

## 二、RAG是什么

RAG是Retrieval-Augmented Generation的缩写，中文通常称为检索增强生成。
它先从知识库中检索与问题相关的内容，再把这些内容提供给模型生成回答。

普通LLM主要根据输入和模型已有知识回答；RAG会额外提供外部知识内容，适合回答指定文档中的问题。

本项目使用余弦相似度只是为了实现一个最小、可理解的RAG示例。RAG的本质是检索相关信息并把它作为上下文提供给模型，不等于某一种固定的相似度算法。

项目18使用普通字符串搜索：

```text
问题 → search_notes() → 字符串匹配 → 返回结果
```

本项目使用向量检索：

```text
问题 → Embedding → 相似度计算 → Top-K → LLM回答
```

## 三、核心概念

- Embedding：把文本转换成一组数字；
- 向量：表示文本特征的一组数字；
- 相似度：衡量两个向量相关程度的数值；
- Top-K：按相似度排序后取最相关的K个结果；
- Retrieval：从知识库中检索相关内容；
- Generation：让LLM根据问题和检索上下文生成回答。

本项目使用`text-embedding-3-small`生成向量，使用`gpt-5.6`生成文本。Embedding模型用于表示和比较文本，生成模型用于生成回答。

## 四、项目结构

```text
19-项目04-RAG基础/
├── README.md
├── main.py
├── config.py
├── documents.py
├── embeddings.py
├── retriever.py
├── llm_client.py
├── rag.py
├── requirements.txt
├── .env.example
└── data/
    └── knowledge/
        ├── python.md
        ├── llm.md
        └── agent.md
```

运行后可能生成`data/index.json`，用于缓存文档文本和向量，避免每次重新生成Embedding。

## 五、安装和运行

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

输入例如：

```text
Python中的函数有什么作用？
```

输入`exit`或`quit`退出。

## 六、上下文构建

检索结果会被整理成包含来源和内容的上下文，并明确告诉模型这些内容来自知识库。
程序要求模型优先依据提供的知识库回答；如果上下文没有相关信息，应说明知识库中没有找到，而不是假装有答案。

## 七、index.json的作用

`index.json`保存每个chunk的`source`、`text`和`embedding`。保存原始文本是为了检索后把内容提供给模型，保存来源是为了知道回答依据来自哪个文档。

这是教学项目，JSON适合保存少量向量。生产环境中大量向量通常会使用向量数据库等基础设施，但向量数据库不是RAG本身。

## 八、当前项目限制

本项目使用固定字符数切分、标准库余弦相似度和JSON缓存，没有复杂分词、重排、向量数据库、混合检索或评估系统。
