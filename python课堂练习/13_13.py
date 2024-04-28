# 给下面代码补充一个初始化方法（其余部分不变），要求最后的打印结果是:你在哪里出生？我出生在广东。
class Chinese:
    def __init__(self, hometown):
        self.hometown = hometown
        print("你在哪里出生？")

    def born(self):
        print('我出生在%s。' % self.hometown)


yanrong = Chinese('广东')
yanrong.born()
