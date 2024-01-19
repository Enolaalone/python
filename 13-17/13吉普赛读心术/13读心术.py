import turtle as t
import random
import time
import Data2


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def p(x, y):
    move(Data2.write2[0], Data2.write2[1])
    t.write(Data2.B[8], align='center', font=('宋体', 120, 'normal'))
    time.sleep(2)
    t.clear()
    process()


def process():
    Data2.B = []
    b = random.randint(0, len(Data2.A) - 1)
    for i in range(100):
        if (i + 1) % 9 == 0:
            Data2.B.append(Data2.A[b])
        else:
            a = random.randint(0, len(Data2.A) - 1)
            Data2.B.append(Data2.A[a])

    t.tracer(0)
    move(Data2.title[0], Data2.title[1])
    t.write('读心术', align='center', font=('宋体', 100, 'normal'))

    move(Data2.circle[0], Data2.circle[1])
    t.color('skyblue')
    t.begin_fill()
    t.circle(Data2.circle[2])
    t.end_fill()

    move(Data2.write[0], Data2.write[1])
    t.color('black')
    t.write(Data2.write[2], align='center', font=('宋体', 12, 'normal'))

    for i in range(10):
        for j in range(10):
            move(80 * j, 300 - 80 * i)
            t.write(Data2.B[j + 10 * i], align='center', font=('宋体', 30, 'normal'))
            move(80 * j, 300 - 80 * i - 40)
            t.write(1 + j + 10 * i, align='center', font=('宋体', 30, 'normal'))
    t.tracer(1)
    t.onscreenclick(p)


t.hideturtle()
t.bgcolor('pink')
process()
t.done()
