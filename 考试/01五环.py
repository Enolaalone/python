import turtle as t

huan1 = [[-280, 180, 120, 'blue'], [0, 180, 120, 'black'], [280, 180, 120, 'red'], [150, 60, 120, 'green'],
         [-150, 60, 120, 'yellow']]
huan2 = [[0, 180, 120, -20, 'black'], [280, 180, 120, -20, 'red'], [0, 420, -120, 100, 'black'],
         [-280, 420, -120, 100, 'blue']]


def move(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()


def huan(x, y, r, color):
    move(x, y)
    t.color(color)
    t.circle(r)


def huan_1(x, y, r, dg, color):
    move(x, y)
    t.color(color)
    t.circle(r, dg)
    t.seth(0)


t.hideturtle()
t.width(20)
t.tracer(0)

for i in range(5):
    huan(huan1[i][0], huan1[i][1], huan1[i][2], huan1[i][3])

for i in range(4):
    huan_1(huan2[i][0], huan2[i][1], huan2[i][2], huan2[i][3], huan2[i][4])
t.tracer(1)
t.done()
