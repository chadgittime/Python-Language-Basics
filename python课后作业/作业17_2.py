import turtle

t = turtle.Pen()


def octagon():
    t.fillcolor('gold')
    t.begin_fill()
    for i in range(1, 9):
        t.forward(60)
        t.right(45)
    t.end_fill()


octagon()
turtle.done()
