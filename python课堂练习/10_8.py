# 直接运行，观察结果
def menu(appetizer, course):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course + '\n')


menu('牛肉拉面', '话梅花生')
menu('话梅花生', '牛肉拉面')
# 如果采用下面这种形式传递，就不需要理会参数位置
menu(course='牛肉拉面', appetizer='话梅花生')
