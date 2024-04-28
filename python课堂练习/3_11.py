historyscore=26

if historyscore>=60:
    print("你已经及格")
    if historyscore>=80:
        print("你可真优秀！")
    elif 60<historyscore<80:
        print("你只是一般般啊兄弟！")
else:
    print("不及格")
print("程序结束")