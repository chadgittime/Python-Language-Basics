#以下是原始代码。优化代码，使它打印出不换行的效果。
for i in range(1,3):
    print('%d X %d = %d' % (i,2,i*2),end="   ")
print()
for i in range(1,4):
    print('%d X %d = %d' % (i,3,i*3),end="   ")
