'''2、该谁给钱（中等）
你为了帮助好朋友小静减肥，和她一起制定了一个饮食游戏。
游戏规则如下：
如果小静一天吃超过10个巧克力，小静要给你100块；
如果小静一天吃小于等于10个的巧克力，你就给小静100块。 
请写出一段代码：当随机从键盘输入小静一天吃的巧克力数量时，可以判断出这天，是小静给你钱，还是你给小静钱，并打印出来。'''

# 我想人工修改题目，我要把巧克力变成溜溜梅！
# 我没事r就吃溜溜梅你别管我啦。

number = int(input("小静到底今天吃了多少块溜溜梅啊！\n请输入数量：\n"))

if number > 10:
    print("你没事就吃溜溜梅？\n你快给我100块！")

elif 0 <= number <= 10:
    print("揍嘛啊，你为什么不多吃点溜溜梅！\n那我只好给你100块了\n你没事r吧？")
