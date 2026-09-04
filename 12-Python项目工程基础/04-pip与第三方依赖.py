# pip与第三方依赖

# Python标准库是Python自带的模块，不需要额外安装。
# 第三方库不是Python默认自带的，需要根据需要安装。

# 例如requests是一个常见的第三方库名称。
# 本章只用它作为认识示例，不在当前项目中实际引入它。

# pip是Python常用的包安装工具。
# 查看当前Python解释器对应的pip版本：
# python -m pip --version

# 安装第三方库：
# python -m pip install requests

# 查看当前环境中已经安装的包：
# python -m pip list

# 卸载第三方库：
# python -m pip uninstall requests

# 使用python -m pip，可以明确使用当前Python解释器对应的pip。

# 如果项目代码中写有：
# import requests
# 那么requests就是这个项目的一个第三方依赖。

# 当前只学习第三方库和pip的基本概念，不安装第三方库，也不展开pip的内部实现。
