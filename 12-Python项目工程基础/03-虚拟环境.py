# 虚拟环境

# 不同Python项目可能需要同一个第三方库的不同版本。
# 如果所有库都安装到同一个环境中，项目之间可能互相影响。
# 虚拟环境可以给不同项目提供相对独立的Python运行环境。

# Python自带venv工具，可以创建虚拟环境。
# 在项目目录中执行：
# python -m venv .venv

# venv是Python自带的虚拟环境工具。
# .venv是常见的虚拟环境目录名称。

# Windows激活虚拟环境：
# .venv\Scripts\activate

# macOS或Linux激活虚拟环境：
# source .venv/bin/activate

# 退出虚拟环境：
# deactivate

# 虚拟环境是项目的运行环境，不是项目源代码本身。
# .venv目录通常不提交到Git仓库。
# 其他人可以根据项目依赖重新创建自己的虚拟环境。

# 当前只了解虚拟环境的用途和基本命令，不展开内部实现。
