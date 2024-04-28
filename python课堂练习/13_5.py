# 创建“中国人”类，并在创建的Chinese类基础上调用属性和实例方法

class Chinese:
    eye = "black"
    skin = "yellow"

    def start(self):
        print("中国人是黄皮肤黑眼睛的")


my_identity = Chinese()
print(type(my_identity))
print(my_identity.eye)
print(my_identity.skin)
my_identity.start()
