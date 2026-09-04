# os与pathlib基础
# Python标准库是Python自带的模块和工具，不需要额外安装。
# 标准库可以帮助我们处理文件、路径、时间和文本等常见任务。

# os模块提供了一些操作系统相关的功能。
# import os
# print(os.getcwd())       # 获取当前工作目录
# print(os.listdir())      # 查看当前目录中的内容
# print(os.path.exists("data.txt"))  # 判断路径是否存在
# print(os.path.isfile("data.txt"))  # 判断是否是文件
# print(os.path.isdir("data"))       # 判断是否是目录
# print(os.path.join("data", "student.txt"))  # 拼接路径

# pathlib提供了面向对象的路径表示方式。
# from pathlib import Path
# path = Path("data")
# print(Path.cwd())
# print(path.exists())
# print(path.is_file())
# print(path.is_dir())
# print(path.name)
# print(path.suffix)
# print(path.parent)

# pathlib使用/拼接路径。
# from pathlib import Path
# path = Path("data")
# file_path = path / "student.txt"
# print(file_path)

# os.path和pathlib都可以处理路径，pathlib的路径操作通常更直观。
# 当前只学习基础路径判断和拼接，不进行文件创建、删除等操作。
