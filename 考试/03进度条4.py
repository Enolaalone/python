import turtle as t

a1 = t.Pen()
a1.hideturtle()
a2 = t.Pen()
a2.hideturtle()
b1 = t.Pen()
b1.hideturtle()
b2 = t.Pen()
b2.hideturtle()

def move(x,y,a):
    a.pu()
    a.goto(x,y)
    a.pd()

t.tracer(0)
move(-100,300,a1)
for _ in range(2):
    a1.fd(200)
    a1.right(90)
    a1.fd(50)
    a1.right(90)

a1.seth(-90)
move(-10,350,a2)
t.tracer(1)

for i in range(200):
    t.tracer(50)
    a2.clear()
    move(-100+(i+1),300,a1)
    a1.fd(50)
    a2.write(f'{(i+1)/2:.1f}%',align='center',font=('宋体',20,'normal'))


b1.width(20)
move(0,-200,b1)
move(0,-100,b2)
for i in range(100):
    t.tracer(50)
    b2.clear()
    b1.circle(100,3.6)
    b2.write(f'{(i+1)}%',align='center',font=('宋体',20,'normal'))

t.done()

