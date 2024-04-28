# 阅读、运行代码，观察结果
class Chinese:
    eye = 'black'

    def eat(self):
        print('吃饭，选择用筷子。')

# 类的实例化：创建多个实例
niuniu = Chinese()
xiangxiang = Chinese()
yanrong = Chinese()

print(xiangxiang.eye)
niuniu.eat()
yanrong.eat()

print("牛牛",end=("")),niuniu.eat()