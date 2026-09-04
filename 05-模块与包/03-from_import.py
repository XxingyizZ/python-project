# from ... import ...
# from 模块 import 名称可以从模块中导入指定的名称。

# import math时，需要通过math.sqrt()访问sqrt函数。
# import math
# print(math.sqrt(16))

# 使用from ... import ...后，可以直接使用导入的名称。
# from math import sqrt
# print(sqrt(16))

# 也可以同时导入多个名称。
# from math import sqrt, pi
# print(sqrt(25))
# print(pi)

# import math和from math import sqrt的主要区别：
# import math会导入模块，使用时写成math.sqrt()。
# from math import sqrt只导入sqrt，使用时直接写sqrt()。

# as可以为模块或导入的名称设置别名。
# import math as m
# print(m.sqrt(16))

# 也可以为导入的名称设置别名。
# from math import sqrt as s
# print(s(16))

# 别名只是当前文件中使用的另一个名称，不会改变模块或函数本身。
