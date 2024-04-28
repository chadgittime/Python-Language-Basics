# 查看注释，运行代码。
import random
import time


def lottery():
    # 用random函数在列表中随机抽奖，列表中只有3位候选者。

    luckylist = ['张涵', '郭悦洋', '牛艺睿', '王思琪']
    # random模块中有个随机选取一个元素的方法：random.choice()。
    luckyone = random.choice(luckylist)  # 从3个人中随机选取1个人。
    print('开奖倒计时', 3)
    time.sleep(1)  # 调用time模块，控制打印内容出现的时间
    print('开奖倒计时', 2)
    time.sleep(1)
    print('开奖倒计时', 1)
    time.sleep(1)
    # 使用三引号打印hellokitty的头像
    image = '''
     /\_)o<
    |      \\
    | O . O|
     \_____/
    '''
    print(image)  # ……
    return luckyone


print("恭喜" + lottery() + "获奖啦！")
