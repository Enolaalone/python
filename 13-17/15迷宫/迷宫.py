import turtle as t

a1 = t.Pen()
b1 = t.Pen()
c1 = t.Pen()
d1 = t.Pen()

d1.color('red')
c1.shape('circle')
b1.color('yellow')
a1.color('red')
c1.color('blue')

d1.pu()
d1.hideturtle()
b1.hideturtle()
a1.hideturtle()
tm = 0
k = True
#
walls = [[-300, 200, -280, 50], [280, 200, 300, 50], [-10, 200, 10, -75], [-200, 200, -180, -75], [180, 200, 200, -75]
    , [-300, -50, -280, -200], [280, -50, 300, -200], [-100, 75, -80, -200], [80, 75, 100, -200],
         [-300, -180, 300, -200], [-300, 200, 300, 180]]  # 存放数据

game = t.Screen()
game.setup(800, 600)
game.title('走迷宫')
game.bgcolor('black')


def move(a, x, y):
    a.pu()
    a.goto(x, y)
    a.pd()


def time_record():
    global tm, k
    t.tracer(0)
    if k:
        tm += 1
    a1.clear()
    move(a1, -10, 240)
    a1.write(f'时间:{tm}', align='center', font=('宋体', 35, 'bold'))
    t.tracer(1)
    t.ontimer(time_record, 1000)


def create_wall(a, b, c, d):
    b1.begin_fill()
    move(b1, a, b)
    b1.goto(c, b)
    b1.goto(c, d)
    b1.goto(a, d)
    b1.goto(a, b)
    b1.end_fill()


def move_up():
    n = 0
    for wall in range(len(walls)):
        if walls[wall][0] - 10 <= c1.xcor() <= walls[wall][2] + 10 and walls[wall][3] - 10 <= c1.ycor() + 4 <= \
                walls[wall][1] + 10:
            continue
        else:
            n += 1
    if n == 11:
        c1.goto(c1.xcor(), c1.ycor() + 4)


def move_down():
    n = 0
    for wall in range(len(walls)):
        if walls[wall][0] - 10 <= c1.xcor() <= walls[wall][2] + 10 and walls[wall][3] - 10 <= c1.ycor() - 4 <= \
                walls[wall][1] + 10:
            continue
        else:
            n += 1
    if n == 11:
        c1.goto(c1.xcor(), c1.ycor() - 4)


def move_right():
    n = 0
    for wall in range(len(walls)):
        if walls[wall][0] - 10 <= c1.xcor() + 4 <= walls[wall][2] + 10 and walls[wall][3] - 10 <= c1.ycor() + 4 <= \
                walls[wall][1] + 10:
            continue
        else:
            n += 1
    if n == 11:
        c1.goto(c1.xcor() + 4, c1.ycor())
        win()


def move_left():
    n = 0
    for wall in range(len(walls)):
        if walls[wall][0] - 10 <= c1.xcor() - 4 <= walls[wall][2] + 10 and walls[wall][3] - 10 <= c1.ycor() + 4 <= \
                walls[wall][1] + 10:
            continue
        else:
            n += 1
    if n == 11:
        c1.goto(c1.xcor() - 4, c1.ycor())


def win():
    global k
    if c1.xcor() >= 285:
        k = False
        d1.goto(-150, 240)
        d1.write('完成!!', align='center', font=('宋体', 35, 'bold'))


t.tracer(0)
move(c1, -300, 0)
c1.pu()
for wall in range(len(walls)):
    create_wall(walls[wall][0], walls[wall][1], walls[wall][2], walls[wall][3])
time_record()
t.tracer(1)

game.listen()
game.onkeypress(move_right, 'Right')
game.onkeypress(move_left, "Left")
game.onkeypress(move_down, 'Down')
game.onkeypress(move_up, 'Up')
t.mainloop()
