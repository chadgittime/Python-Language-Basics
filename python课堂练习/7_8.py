# 请先阅读代码，然后直接运行，观察结果
a = 1
b = -1

print('以下是and运算')
if a==1 and b==1:    # 【b实际上是-globaltimes】
    print('True')
else:
    print('False')

print('以下是or运算')
if a==1 or b==1:  # 【b实际上是-globaltimes】
    print('True')
else:
    print('False')
