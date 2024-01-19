import math
import turtle as t


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def under(w, x, y):
    move(x, y)
    t.color('red')
    t.begin_fill()
    for i in range(2):
        t.fd(3 * (w / 2))
        t.right(90)
        t.fd(w)
        t.right(90)
    t.end_fill()


def star(size):
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.right(144)
    t.end_fill()


def big_star(size, x, y):
    move(x, y)
    t.seth(-72)
    star(size)


def small_star(size, x0, y0, dg, distance):
    move(x0, y0)
    t.seth(dg)
    t.pu()
    t.fd(distance)
    t.pd()
    t.left(15)
    star(size)


def flag(w, x, y):
    t.hideturtle()
    under(w, x, y)
    big_star(6 * (w / 20) * math.cos(15 * math.pi / 180), -(3 * w / 4) * (10 / 15), (8 / 10) * w / 2)

    small_star(2 * (w / 20) * math.cos(15 * math.pi / 180), -(3 * w / 4) * (10 / 15), w / 4,
               math.degrees(math.atan(3 / 5)), ((5 * w / 20) / (math.cos(math.atan(3 / 5)))) - (w / 20))
    small_star(2 * (w / 20) * math.cos(15 * math.pi / 180), -(3 * w / 4) * (10 / 15), w / 4,
               math.degrees(math.atan(1 / 7)), ((7 * w / 20) / (math.cos(math.atan(1 / 7)))) - (w / 20))
    small_star(2 * (w / 20) * math.cos(15 * math.pi / 180), -(3 * w / 4) * (10 / 15), w / 4,
               -math.degrees(math.atan(2 / 7)), ((7 * w / 20) / (math.cos(math.atan(1 / 7)))) - (w / 20))
    small_star(2 * (w / 20) * math.cos(15 * math.pi / 180), -(3 * w / 4) * (10 / 15), w / 4,
               -math.degrees(math.atan(4 / 5)), ((5 * w / 20) / (math.cos(math.atan(4 / 5)))) - (w / 20))


t.tracer(0)

flag(400, -300, 200)

t.tracer(1)
t.done()
