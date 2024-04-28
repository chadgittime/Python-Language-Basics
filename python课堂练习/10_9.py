# 直接运行，观察结果
def menu(appetizer, course, dessert='绿豆沙'):
    print('一份开胃菜：' + appetizer)
    print('一份主食：' + course)
    print('一份甜品：' + dessert)


menu('话梅花生', '牛肉拉面')
# 因为已经默认将'绿豆沙'传递给dessert，调用时无须再传递。
