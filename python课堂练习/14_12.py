# 请通过参数默认值的改变完成下面子类的定制，让程序的运行结果为“雷猴！欢迎来到广东。”
# 提示：初始化方法的定制，和一般的实例方法的定制是一样的。
class Chinese:
    def __init__(self, greeting='你好', place='中国'):
        self.greeting = greeting
        self.place = place

    def greet(self):
        print('{},欢迎来到{}!'.format(self.greeting, self.place))


# 请为子类完成定制，代码量：两行。
class Cantonese(Chinese):
    def __init__(self, greeting='雷猴', place='广东'):
        Chinese.__init__(self, greeting, place)


# 去调用父类的方法

yewen = Cantonese()
yewen.greet()
