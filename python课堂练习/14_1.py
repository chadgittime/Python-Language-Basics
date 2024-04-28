# 请为下列代码加上注释，然后再运行
class Chinese:  # 类的创建
    eye = 'black'  # 类属性的创建

    def __init__(self, hometown):  # 类的初始化方法
        self.hometown = hometown  # 实例属性的创建
        print('程序持续更新中⋯⋯')  # 初始化中的语句

    def born(self):  # 实例方法born的创建
        print('我生在%s。' % self.hometown)  # 方法的具体语句


yanrong = Chinese('广东')  # 类的实例化
print(yanrong.eye)  # 打印实例的属性（从类传递的）
yanrong.born()  # 调用实例方法born
