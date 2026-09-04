# requirements.txt与依赖管理

# requirements.txt通常是一个文本文件，用来记录项目依赖及其版本信息。

# 例如文件内容可以是：
# requests==2.32.3

# 这表示项目记录了requests及其版本。
# 当前只做认识，不要求安装这个示例依赖。

# 将当前环境中已经安装的包记录到requirements.txt：
# python -m pip freeze > requirements.txt

# 根据requirements.txt安装项目依赖：
# python -m pip install -r requirements.txt

# 依赖管理的基本过程：
# 开发环境中的依赖
#         ↓
# 记录到requirements.txt
#         ↓
# 其他环境根据记录安装

# 依赖文件可以帮助其他人了解项目需要哪些第三方库。
# 本章不展开Poetry、uv和pip-tools等其他依赖管理工具。
