import turtle
t=turtle.Pen()
a=turtle.Pen()

def tiao(c):
    t.color(f'{c}')
    t.begin_fill()
    for i in range(2):
        t.fd(494)
        t.right(90)
        t.fd(20)
        t.right(90)
    t.end_fill()

def star():
    a.right(72)
    a.color('white')
    a.begin_fill()
    for i in range(5):
        a.fd(12)
        a.right(144)
    a.end_fill()
    a.right(-72)

def star6():
    a.pu()
    a.fd(20)
    a.pd()
    star()
    for i in range(5):
        a.pu()
        a.fd(40)
        a.pd()
        star()

def star5():
    a.pu()
    a.fd(40)
    a.pd()
    star()
    for i in range(4):
        a.pu()
        a.fd(40)
        a.pd()
        star()

turtle.tracer(0)
a.hideturtle()
t.hideturtle()


for i in range(14):
    if i%2==1:
        color='white'
    else:
        color='red'
    tiao(color)
    t.right(90)
    t.fd(20)
    t.left(90)


t.up()
t.home()
t.down()
t.color('blue')
t.begin_fill()
for i in range(2):
    t.fd(240)
    t.right(90)
    t.fd(140)
    t.right(90)
t.end_fill()

for i in range(9):
    a.pu()
    a.home()
    a.right(90)
    a.fd(i*14+7)
    a.left(90)
    a.pd()
    if i%2==0:
        star6()
    else:
        star5()

turtle.tracer(1)
turtle.done()