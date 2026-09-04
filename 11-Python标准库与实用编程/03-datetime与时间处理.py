# datetime与时间处理
# datetime模块用于处理日期和时间。
# from datetime import datetime, date, time, timedelta

# date表示日期，time表示时间，datetime表示日期和时间，timedelta表示时间间隔。

# 获取当前日期和时间。
# now = datetime.now()
# today = date.today()
# print(now)
# print(today)

# 创建指定的日期和时间。
# start_time = datetime(2026, 1, 1, 12, 30)
# print(start_time)

# 获取日期时间中的常见信息。
# now = datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)

# 使用timedelta进行简单的时间计算。
# now = datetime.now()
# tomorrow = now + timedelta(days=1)
# yesterday = now - timedelta(days=1)
# print(tomorrow)
# print(yesterday)

# strftime()可以把日期时间格式化为字符串。
# now = datetime.now()
# time_text = now.strftime("%Y-%m-%d %H:%M:%S")
# print(time_text)

# 常见格式符：%Y表示四位年份，%m表示月份，%d表示日期，
# %H表示小时，%M表示分钟，%S表示秒。

# strptime()可以把符合格式的字符串转换成datetime对象。
# time_text = "2026-01-01 12:30:00"
# start_time = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S")
# print(start_time)

# 当前只学习基础日期时间处理，不展开时区和夏令时。
