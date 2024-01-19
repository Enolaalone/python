import math
import turtle as t
#-------移动笔头---------
def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()


def eyes(x,y,r):
    move(x+r/3,math.sqrt(3)/3*r+y-r/6)
    t.circle(r/6)
    move(x+r/3,math.sqrt(3)/3*r+y-r/6)

    t.fillcolor('black')
    t.begin_fill()
    t.circle(r/12)
    t.end_fill()

    move(x - r / 3, math.sqrt(3) / 3 * r + y - r / 6)
    t.circle(r / 6)
    move(x - r / 3, math.sqrt(3) / 3 * r + y - r / 6)

    t.fillcolor('black')
    t.begin_fill()
    t.circle(r / 12)
    t.end_fill()

def happy2(x,y,r):

#-------画脸--------
    move(x,y-r*2/3)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()
#----眼睛----------

    eyes(x,y,r)

#-----歪嘴-------------
    move(x - r / 3, -(math.sqrt(3) / 3 * r + y) + r / 6)
    t.right(30)
    t.circle(r * 2 / 3, 120)



happy2(0,0,100)
t.done()