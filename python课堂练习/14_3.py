# 为下面父类Cat创建一个子类Ragdoll(布偶猫)，并用这个子类的实例来调用父类的属性和方法。

class Cat:
    tail = True

    def say(self):
        print('喵喵喵喵喵~')

class Ragdoll(Cat):
    pass

ragdoll=Ragdoll()
print(ragdoll.tail)
ragdoll.say()