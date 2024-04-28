#直接运行，运行两次：第1次.连续五次不输入零；第2次.输入一次0跳出循环，观察结果。

for i in range(5):
    a = int(input('请输入0来结束循环，你有5次机会:'))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')
        break
else:
    print('5次循环你都错过了，else语句生效了。')
