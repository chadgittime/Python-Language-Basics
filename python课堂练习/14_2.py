# 阅读代码，再运行代码
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')


class Cantonese(Chinese):
    # 通过继承，Chinese类有的，Cantonese也有
    pass  # pass表示'跳过'，不执行其他操作


# 验证子类可以继承父类的属性和方法，进而传递给子类创建的实例
yewen = Cantonese()
# 子类创建的实例，从子类那间接得到了父类的所有属性和方法
print(yewen.eye)
# 子类创建的实例，可调用父亲的属性
yewen.eat()
# 子类创建的实例，可调用父亲的方法
