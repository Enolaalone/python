import turtle
import time
def move(x,y,a):
    a.speed(0)
    a.up()
    a.goto(x,y)
    a.pd()
turtle.hideturtle()
a1=turtle.Pen()
b1=turtle.Pen()
a1.hideturtle()
b1.hideturtle()
a=turtle.Pen()
b=turtle.Pen()
a.hideturtle()
b.hideturtle()

turtle.tracer(0)
a1.up()
a1.hideturtle()
a1.goto(-50,300)
a1.pd()

for i in range(2):
    a1.fd(100)
    a1.right(90)
    a1.fd(40)
    a1.right(90)

a1.seth(90)
move(-50,260,a1)
turtle.tracer(1)
move(-20,300,b1)
n=0
for i in range(100):
    a1.fd(40)
    n+=1
    move(-50+n,260,a1)
    k=n
    b1.write(f'{k}%',font=('宋体',20,'normal'))
    turtle.tracer(100)
    time.sleep(0.2)
    b1.clear()

a1.clear()
b1.clear()

b.up()
b.goto(-50,200)
b.pd()
a.width(10)

n=0
for i in range(36):
    n+=10
    a.circle(200,10)

    k=10*n/(36)
    b.write(f'{k:.2f}%',font=('宋体',30,'normal'))
    turtle.tracer(100)
    time.sleep(0.25)
    b.clear()



turtle.done()