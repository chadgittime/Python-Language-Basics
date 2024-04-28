# 阅读运行代码
import turtle

t = turtle.Pen()


def mycircle(red, green, blue):
    t.begin_fill()  # 准备填充
    t.circle(150)  # 50指的是半径
    t.color(red, green, blue)
    t.end_fill()  # 填充完毕


mycircle(0, 0.5, 0.5)
turtle.done()
