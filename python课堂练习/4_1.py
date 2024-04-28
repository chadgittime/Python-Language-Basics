#直接运行，输入你选的数字，再按回车。

import time

print('亲爱的同学：')
time.sleep(1)

print('我们愉快地通知您，您已获准在霍格沃茨魔法学校就读。')
time.sleep(2)

print('随信附上所需书籍及装备一览。')
time.sleep(1)

print('学期定于九月一日开始。')
time.sleep(1)

print('鉴于您对魔法世界的不熟悉，')
time.sleep(1)

print('我们将指派魔咒学老师——弗立维教授带您购买学习用品。')
time.sleep(2)

print('我们将于七月三十一日前静候您的猫头鹰带来的回信。')
time.sleep(2)

print('校长（女）米勒娃·麦格谨上')
time.sleep(1)

print('那么，您的选择是什么？ globaltimes 接受，还是 2 放弃呢？')
time.sleep(2)

choice = input('请输入您选择的数字：')

if choice == 'globaltimes':
    print('霍格沃茨欢迎您的到来。')

else:
    print('您可是被梅林选中的孩子，我们不接受这个选项。')
