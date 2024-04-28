# 阅读、运行代码，观察结果

class Chinese:
    name = '牛牛'  # 类属性name

    def say(self, who, nation):  # 带有两个参数的方法
        print(who + '是' + nation)


person = Chinese()
print(person.name)
person.say('郭悦洋', '中国人')
# self调用时要忽略，'牛牛'传给参数someone
