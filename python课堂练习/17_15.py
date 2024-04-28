import time
import turtle

t1 = turtle.Pen()


def square():
    global t1
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(100)


def parallel():
    t1.forward(100)
    t1.up()
    t1.right(90)
    t1.forward(20)
    t1.down()
    t1.right(90)
    t1.forward(100)

square()
time.sleep(3)
t1.reset()
parallel()
turtle.done()
