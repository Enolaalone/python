import time
import turtle as t
game=t.Screen()
game.setup(800,600)


t.tracer(0)
star_time = time.time()

e=t.Pen()
e.hideturtle()

c=t.Pen()
c.hideturtle()
e.color('red')

c.up()
e.up()
c.goto(-70, 250)
e.goto(-70, 250)
c.left(-90)
t.tracer(1)
while(1):
    end_time=time.time()
    t.tracer(False)
    c.color('white')
    c.begin_fill()
    for i in range(2):
        c.fd(20)
        c.left(90)
        c.fd(150)
        c.left(90)
        c.fd(40)
    c.end_fill()
    e.write(f'耗时：{end_time-star_time:.2f}',font=('宋体',20,'normal'))
    t.tracer(True)





