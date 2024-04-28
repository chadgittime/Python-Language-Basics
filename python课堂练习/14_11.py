# 阅读代码后运行，观察结果
class Chinese:

    def land_area(self, area):
        print('我们居住的地方，陆地面积是%d万平方公里左右。' % area)


class Cantonese(Chinese):
    # 为参数 area 设置默认值。
    def land_area(self, area=960, rate=0.0188):
        Chinese.land_area(self, area * rate)


yewen = Cantonese()
yewen.land_area()
# 两个参数都有默认值，所以可以这么调用。
