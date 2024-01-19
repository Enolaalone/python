#初始界面----------------------

import turtle
def move(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
def river(x,y):
    move(x,y)
    turtle.color('skyblue')
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(600)
        turtle.right(90)
        turtle.fd(1200)
        turtle.right(90)
    turtle.end_fill()
turtle.register_shape('lang.gif')#注册turtle
turtle.register_shape('yang.gif')
turtle.register_shape('cai.gif')
turtle.register_shape('chuan.gif')
a=turtle.Pen()
b=turtle.Pen()
c=turtle.Pen()
d=turtle.Pen()
a.shape('lang.gif')
b.shape('cai.gif')
c.shape('yang.gif')
d.shape('chuan.gif')
a.up()
b.up()
c.up()
d.up()
he=[[],[],[]]
p=[[-450,200],[-450,0],[-450,-200],[450,200],[450,0],[450,-200]]

turtle.tracer(0)
river(-300,600)
a.goto(p[0][0],p[0][1])
b.goto(p[1][0],p[1][1])
c.goto(p[2][0],p[2][1])


turtle.tracer(1)
turtle.done()