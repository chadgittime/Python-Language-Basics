# 阅读代码再运行。
class Chinese:
    pass

class Cantonese(Chinese):
    pass

gonger = Chinese()
# 宫二，电影《一代宗师》女主，生于东北
yewen = Cantonese()
# 叶问，电影《一代宗师》男主，生于广东

print('\n验证1：子类创建的实例同时也属于父类')
print(isinstance(gonger,Chinese))
print(isinstance(yewen,Chinese))

print('\n验证2：父类创建的实例不属于子类。')
print(isinstance(gonger,Cantonese))

print('\n验证3：类创建的实例都属于根类。')
print(isinstance(gonger,object))
print(isinstance(yewen,object))
