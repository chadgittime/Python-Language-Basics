# 补全下面代码，将元组中的两个元素分别打印出来。
import random

appetizer = ['话梅花生', '拍黄瓜', '凉拌三丝']


def coupon(money):
    if money < 5:
        a = random.choice(appetizer)
        return a
    elif 5 <= money < 10:
        b = random.choice(appetizer)
        return b, '溏心蛋'


result = coupon(6)
# result是一个元组

for i in result:
    print(i)
