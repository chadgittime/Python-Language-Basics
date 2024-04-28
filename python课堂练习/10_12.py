#直接运行，观察结果
def menu(*barbeque):
    for i in barbeque:
        print('一份烤串：' + i)

menu('烤香肠', '烤肉丸')
menu('烤鸡翅', '烤茄子', '烤玉米')
# 不定长参数可以接收任意数量的值
