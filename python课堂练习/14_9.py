# 阅读运行代码
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')


class Cantonese(Chinese):  # 类的继承
    native_place = '广东'  # 类的定制

    def dialect(self):  # 类的定制
        print('我们会讲广东话。')


yewen = Cantonese()
print(yewen.eye)
# 父类的属性能用
print(yewen.native_place)
# 子类的定制属性也能用
yewen.eat()
# 父类的方法能用
yewen.dialect()
# 子类的定制方法也能用
