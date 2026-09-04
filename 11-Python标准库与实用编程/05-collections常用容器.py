# collections常用容器
# collections模块提供了一些常用的数据容器。

# Counter可以统计元素出现的次数。
# from collections import Counter
# words = ["python", "java", "python", "go", "python"]
# counter = Counter(words)
# print(counter)
# print(counter["python"])
# print(counter.most_common())

# defaultdict访问不存在的key时，可以自动创建默认值。
# from collections import defaultdict
# groups = defaultdict(list)
# groups["A"].append("Tom")
# groups["A"].append("Jack")
# groups["B"].append("Lucy")
# print(groups)

# deque适合在两端添加和删除元素。
# from collections import deque
# queue = deque(["小明", "小红"])
# queue.append("小刚")
# queue.appendleft("小李")
# print(queue)
# print(queue.popleft())
# print(queue.pop())
# print(queue)

# deque可以作为简单的队列使用：一端加入数据，另一端取出数据。
# 当前只学习Counter、defaultdict和deque的基础用法，不展开collections的其他内容。
