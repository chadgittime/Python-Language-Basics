#编写“猜大小游戏”代码：一个人在心里想好一个数，如24，然后让另一个人猜。如果猜的数比24小，告诉他“太小了”，如果猜的数比24大，告诉他“太大了”。
for i in range(3):
    number=int(input("你猜猜我的年龄是多少：\n"))
    if number>19:
        print("数大了，你再猜试试。")
    elif number<19:
        print("数小了，你再猜试试。")
    else:
        print("恭喜你猜对了，我今年19岁！")
        break
else:
    print("三次机会你都没打对，你失败了！")