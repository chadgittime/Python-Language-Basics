# 直接运行，观察运行结果
def menu(*barbeque):
    return barbeque
#星号的意思是可以输入多个

order = menu('烤鸡翅', '烤茄子', '烤玉米')

print(order)
print(type(order))
