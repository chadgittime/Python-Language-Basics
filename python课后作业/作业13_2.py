# 这个代码只要用到类中的初始化方法和类的实例化。

class Robot:
    def __init__(self):
        robot_name = input("请您给机器人命名：\n")
        user_name = input("请输入您的称呼：\n")
        print("你好，{}。我是{}。遇见你，真好。".format(user_name, robot_name))


robot1 = Robot()


# 请将你在上一步写好的代码复制黏贴，在其基础上增加实例方法。

class Robot:
    def __init__(self):
        robot_name = input("请您给机器人命名：\n")
        user_name = input("请输入您的称呼：\n")
        print("你好，%s。我是%s。遇见你，真好。" % (user_name, robot_name))

    def say_wish(self):
        wish = input("我有一个愿望:\n")
        for i in range(1, 4):
            print(wish)


robot2 = Robot()
robot2.say_wish()
