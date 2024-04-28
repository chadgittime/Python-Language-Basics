# 阅读、运行代码，观察结果

class Chinese:
    def __init__(self):
        self.mouth = 1  # self.不能丢
        self.eye = 2

    def body(self):
        print('我有%s张嘴巴' % self.mouth)
        print('我有%s只眼睛' % self.eye)


person = Chinese()
person.body()
