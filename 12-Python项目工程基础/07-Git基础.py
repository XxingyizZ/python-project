# Git基础

# Git是一种版本控制工具，用来记录项目文件的变化。
# Python项目使用Git后，可以查看过去的版本和代码变化。

# 一个常见的变化过程：
# 今天代码可以运行
#       ↓
# 修改代码
#       ↓
# 出现问题
#       ↓
# 查看之前的版本

# 在项目目录中初始化Git仓库：
# git init

# 查看当前仓库状态：
# git status

# 将文件加入暂存区：
# git add .

# 创建一次提交：
# git commit -m "first commit"

# 查看提交历史：
# git log

# .gitignore用于说明哪些文件通常不提交到Git仓库。
# 一个简单的.gitignore示例：
# .venv/
# __pycache__/
# *.pyc
# .env

# .venv是本地虚拟环境，__pycache__和.pyc是Python缓存文件，
# .env可能包含本地敏感配置，因此通常不提交。

# 当前只学习Git的基本概念和命令，不学习rebase、冲突解决和Git内部实现。
