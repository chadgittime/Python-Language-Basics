'''globaltimes、宠物取名（入门）
请写一段代码，为你的宠物起个名字，并打印出结果【xx（xx是你的名字）的宠物叫做XX】（其中，XX是你起的名字，从键盘输入）。'''

name1 = input("请为你的宠物起个名字吧～\n它的名字是：\n")

answer = input("还有第二只宠物吗？\n请回答'yes'or'no':\n")

if answer == "yes":
    name2 = input("那么请输入这只小可爱的名字：\n")
    print("郭悦洋的宠物们叫做" + name1 + "与" + name2)
else:
    print("郭悦洋的宠物名字是" + name1)
    exit()
