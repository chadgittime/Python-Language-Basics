# 观察代码，然后直接运行代码看看是什么结果

# continue语句搭配for循环
for i in range(5):
    print('明日复明日')
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')

# continue语句搭配while循环
i = 0
while i<5:
    print('明日复明日')
    i = i+1
    if i==3:  # 当i等于3的时候触发
        continue # 回到循环开头
    print('这句话在i等于3的时候打印不出来')
