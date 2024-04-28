# 新建一个方法，让实例只要调用一个方法，就能打印出两个信息。
# 代码完成后，请运行一下，验证是否成功。
class Chinese:

    def __init__(self, hometown, region):
        self.hometown = hometown
        self.region = region
        print('程序持续更新中……')

    def born(self):
        print('我生在%s。' % self.hometown)

    def live(self):
        print('我在%s。' % self.region)

    def main(self):
        self.born()
        self.live()


me = Chinese("北京", "北京")
me.main()
