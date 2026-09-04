# #通过type()函数可以查看变量的类型，函数返回值是一个类型对象
# num = 114.1
# print(type(num)) #<class 'float'>
# print(type(100)) #<class 'int'>
# print(type("Hello, World!")) #<class 'str'>
# print(type(True)) #<class 'bool'>
# print(type(None)) #<class 'NoneType'>
# print(type(num + 1)) #<class 'float'>，num是float类型，1是int类型，float和int类型相加结果是float类型
# print(type(num + 1.0)) #<class 'float'>，num是float类型，1.0是float类型，float和float类型相加结果是float类型
# print(type(num + True)) # <class 'float'> #bool 是 int 的子类，True 在算术运算中相当于 1，False 相当于 0


# #通过isinstance()函数可以判断变量是否是某个类型，函数返回值是一个布尔值
# num = 114.1
# print(isinstance(num, float)) #True
# print(isinstance(num, int)) #False


#字符串的三种定义方式
#双引号定义
str1 = "Hello, World!"
#单引号定义
str2 = 'Hello, World!'
#三引号定义:可以表示多行字符串
str3 = """
Hello, World:
    This is a multi-line string.
    It can span multiple lines.
"""


# #字符串的转义字符

#在字符串中使用反斜杠\来表示转义字符，常用的转义字符有：
# \n：换行
# \t：制表符
# \\：反斜杠
# \'：单引号
# \"：双引号
# str4 = "Hello, World!\nThis is a new line.\n\tThis is a tab."
# print(str4)

# str5 = "Hello的意思是'你好'，World的意思是\"世界\"。"
# print(str5)


# #字符串拼接
# str6 = "情人游天地"
# str7 = "日月换行李"
# print("《我们万岁》歌词里写到:", str6+ ',' + str7)


# 字符串的格式化输出

# #使用%进行格式化输出
# name = "Alice"
# age = 25
# print("My name is %s, and I am %d years old." % (name, age))

# #使用format()方法进行格式化输出
# name = "Bob"
# age = 30
# print("My name is {}, and I am {} years old.".format(name, age))

# #使用f-string进行格式化输出（Python 3.6及以上版本）
# name = "Charlie"
# age = 35
# print(f"My name is {name}, and I am {age} years old.")