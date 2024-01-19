import turtle as t
def square(color):
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.fd(20)
        t.right(90)
    t.end_fill()
    t.color('black')
    for i in range(4):
        t.fd(20)
        t.right(90)

t.hideturtle()
t.tracer(0)
for i in range(10):
    for j in range(10):
        if i%2==0:
            if j%2==0:
                clr='white'
            else:
                clr='black'
        else:
            if j%2==0:
                clr='black'
            else:
                clr='white'
        square(clr)
        t.fd(20)
    t.pu()
    t.goto(0,-20*(i+1))
    t.pd()
t.tracer(1)

t.done()