# 把下面的for循环的代码改成while循环，要求运行效果相同

i=5
while i>0:
    i=i-1
    a = int(input('请输入0结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')
