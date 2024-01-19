import turtle as t

ls = [[69, 15], [292, 10], [33, 8], [131, 10], [61, 5], [254, 10], [100, 15], [80, 25]]


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def XY(x, y):
    move(x, y)
    t.fd(500)
    move(x, y)
    t.seth(90)
    t.fd(300)
    move(x, y)


def form(x, y):
    XY(x, y)
    for i in range(len(ls)):
        move(x + 50 * (i + 1), y)
        for j in range(ls[i][1]):
            t.fd(ls[i][0])
            move(x + 50 * (i + 1) + j, y)

t.tracer(0)
form(-200,-100)
t.tracer(1)
t.done()