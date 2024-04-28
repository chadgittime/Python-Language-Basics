# 【文件：B.py】
a = '我是模块中的变量a'


def hi():
    a = '我是函数里的变量a'
    print('函数“hi”已经运行！')


class Go2:
    a = '我是类2中的变量a'

    def do2(self):
        print('函数“do2”已经运行！')


if __name__ == '__main__':
    print('是主模块的时候才会执行以下语句：')
    print(a)
    hi()
    b = Go2()
    print(b.a)
    b.do2()
