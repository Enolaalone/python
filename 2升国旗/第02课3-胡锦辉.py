import turtle
import time
t = turtle.Turtle()

#-----------画心函数-----------
def xin(x):
    t.penup()
    t.goto(0,x/-1.4)
    t.pendown()
    t.color('red')
    t.begin_fill()
    t.left(45)
    t.forward(x)
    t.circle(x / 2, 180)  # 画圆形，半径，圆心角
    t.right(90)
    t.circle(x / 2, 180)
    t.forward(x)
    t.left(45)
    t.end_fill()


#--------定义画笔---------
t.pencolor("red")
t.pensize(5)
t.speed(9999)

#-----------跳动的心------------
while (1):
    time.sleep(0.1)
    xin(100)
    time.sleep(0.1)
    t.clear()
    xin(200)
    time.sleep(0.1)
    t.clear()
    xin(300)


#结束
turtle.done()