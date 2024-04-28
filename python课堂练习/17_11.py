# 阅读运行代码
import random  # 调用random模块

a = random.random()  # 随机从0-1之间（包括0不包括1）抽取一个小数
print(a)

a = random.randint(0, 100)  # 随机从0-100（包括0和100）之间抽取一个数字
print(a)

a = random.choice('abcdefg')  # 随机从字符串，列表等对象中抽取一个元素（可能会重复）
print(a)

a = random.sample('abcdefg', 3)  # 随机从字符串，列表等对象中抽取多个不重复的元素
print(a)

items = [1, 2, 3, 4, 5, 6]  # “随机洗牌”，比如打乱列表
random.shuffle(items)
print(items)
