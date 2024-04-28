#阅读运行代码，观察结果
class Chinese:
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% area)

class Cantonese(Chinese):
    # 直接对方法进行重写
    def land_area(self,area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。'% int(area*0.0188))

gonger = Chinese()
yewen = Cantonese()
gonger.land_area(960)
yewen.land_area(960)
