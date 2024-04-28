#阅读、运行代码，观察结果

class Chinese:

    def __init__(self, name, birth, region):
        self.name = name   # self.name = '牛牛'
        self.birth = birth  # self.birth = '湖南'
        self.region = region  # self.region = '北京'

    def born(self):
        print(self.name + '出生在' + self.birth)

    def live(self):
        print(self.name + '居住在' + self.region)

person = Chinese('牛牛','湖南','北京') # 传入初始化方法的参数
person.born()
person.live()
