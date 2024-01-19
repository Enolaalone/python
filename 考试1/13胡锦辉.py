import turtle as t
t.hideturtle()
t.tracer(0)
t.up()
t.goto(-200,200)
t.down()
def move(x,y):
    t.up()
    t.goto(x, y)
    t.down()
def white():
    for i in range(4):
        t.fd(25)
        t.right(90)
def black():
    t.color('black')
    t.begin_fill()
    for i in range(4):
        t.fd(25)
        t.right(90)
    t.end_fill()

for j in range(8):
    if j%2==0:
        for i in range(8):
            if i%2==0:
                white()
            else:
                black()
            t.fd(25)
        move(-200,200-25*(j+1))
    else:
        for i in range(8):
            if i % 2 == 0:
                black()
            else:
                white()
            t.fd(25)
        move(-200,200-25*(j+1))



t.tracer(1)
t.done()