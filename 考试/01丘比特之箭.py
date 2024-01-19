import turtle as t
import time


def arrow():
    Screen = t.Screen()
    t.tracer(0)
    t.color('pink')
    t.shape('classic')
    t.shapesize(2, 2)
    while True:
        t.pd()
        t.fd(80)
        t.tracer(0)
        time.sleep(0.05)
        t.clear()
        t.tracer(1)
        if t.xcor() > 400:
            t.tracer(0)
            t.pu()
            t.goto(-400, 0)
            t.tracer(1)


arrow()
