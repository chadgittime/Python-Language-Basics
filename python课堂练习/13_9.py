# 阅读、运行代码，观察结果

class Chinese:

    def greeting(self):
        print('很高兴遇见你')

    def say(self):
        self.greeting()
        print('我来自中国')


person = Chinese()
# 创建实例person
person.say()
# 调用say()方法
