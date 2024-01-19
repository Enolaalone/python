import turtle as t
import time
import math
t.hideturtle()


def move(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()


def heart(size):
    t.width(3)
    t.seth(0)
    t.tracer(0)
    t.color('red')
    t.begin_fill()
    for i in range(2):
        move(0,size/math.sqrt(2))
        if i==0:
            t.left(45)
            t.circle(-size/2,180)
        else:
            t.right(90)
            t.circle(size/2,180)
        t.fd(size)
    t.end_fill()
    t.tracer(1)


while True:
    for i in range(1,3):
        heart(100*i)
        time.sleep(0.15)
        t.clear()

t.done()