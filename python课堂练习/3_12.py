# 根据下面提示续写else条件里的代码：
# 额外条件1：当历史成绩小于60，同时还小于30时，输出结果学渣；
# 额外条件2：当历史成绩小于60，但大于等于30时，输出结果还能抢救一下。

historyscore = 26

if historyscore >= 60:
    print('你已经及格')

    if historyscore >= 80:
        print('你很优秀')

    else:
        print('你只是一般般')

else:
    print('不及格')

    if historyscore<30:
        print("你真是个学渣！")
    elif historyscore>=30:
        print("你还能抢救一下。。。")
    # 增加额外条件if...

print('程序结束')
