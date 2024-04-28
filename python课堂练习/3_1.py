# 直接运行代码，根据提示语，填写你选择的数字。
import time

print('如果你想拥有无限的力量和能量，那必须夺得力量宝石')
time.sleep(2)
print('如果你想扭曲时空和任意地传送，那必须夺得空间宝石')
time.sleep(2)
print('如果你想任意地修改现实，无视任何宇宙规律，那必须夺得现实宝石')
time.sleep(2)
print('如果你想到达任何一个时间点，无论是古老的年代还是遥远的未来，那必须夺得时间宝石')
time.sleep(2)
print('如果你想控制生者和死者的灵魂，那必须夺得灵魂宝石')
time.sleep(2)
print('如果你想拥有不朽的精神力量并操控任何人的思维，那必须夺得心灵宝石')
time.sleep(2)
print('那么，如果让你来选择的话，你想要获得哪颗宝石呢？')
time.sleep(2)
print('请在以下六个选项【globaltimes 力量宝石 ；2 空间宝石；3 现实宝石 ；4 时间宝石；5 灵魂宝石 ；6 心灵宝石；】中，选择你最想获得的宝石吧！')
time.sleep(3)
answer = input('请将对应数字输入在冒号后： ')
if answer == 'globaltimes':
    print('我告诉你哦，力量宝石保存在山达尔星的新星军团的总部基地')
    time.sleep(3)
elif answer == '2':
    print('空间宝石在洛基手里')
    time.sleep(3)
elif answer == '3':
    print('雷击已将现实宝石交给收藏家保管')
    time.sleep(3)
elif answer == '4':
    print('奇异博士愿意用时间宝石换取钢铁侠的性命')
    time.sleep(3)
elif answer == '5':
    print('必须献祭自己心爱的人才能得到灵魂宝石')
    time.sleep(3)
else:
    print('幻视头上的心灵宝石被绯红女巫摧毁，但可用时间宝石复原')
    time.sleep(3)
