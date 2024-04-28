#运行代码，观察结果

class Su:
    born_city = 'Jiangsu'
    wearing = 'thick'  # 穿得较厚

    def diet(self):
        print('我们爱吃甜。')

class Yue:
    settle_city = 'Guangdong'
    wearing = 'thin'  # 穿得较薄

    def diet(self):
        print('我们吃得清淡。')

class Yuesu(Yue,Su):
    pass

xiaoming = Yuesu()
print(xiaoming.wearing)
print(xiaoming.born_city)
xiaoming.diet()
