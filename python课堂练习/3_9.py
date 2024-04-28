#直接运行
historyscore = 26

if historyscore >= 60:
    print('你已经及格')

    if historyscore >= 80:
        print('你很优秀')

    else:
        print('你只是一般般')

else:
    print('不及格')

    if historyscore < 30:
        print('学渣')

    else:
        print('还能抢救一下')

print('程序结束')
