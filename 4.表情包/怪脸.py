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

def g_eye(x,y,r):
    move(x+r/3,math.sqrt(3)/3*r+y-r/6)
    t.circle(r/6)

    move(x+r/3+(r/(6*math.sqrt(2))/2),math.sqrt(3)/3*r+y-r/(6*math.sqrt(2)))
    t.fillcolor('black')
    t.begin_fill()
    t.circle(r/12)
    t.end_fill()

    #----------------------------------------

    move(x - r / 3, math.sqrt(3) / 3 * r + y - r / 6)
    t.circle(r / 6)

    move(x - r / 3-(r/(6*math.sqrt(2))/2), math.sqrt(3) / 3 * r + y)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(r / 12)
    t.end_fill()
def happy3(x,y,r):

#-------画脸--------
    move(x,y-r*2/3)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()




    g_eye(x,y,r)

    move( -math.sqrt(3) / 3 * r +x,y- r / 3+r/6)
    t.right(60)
    t.circle(r*2/3,120)
    t.right(60)




happy3(0,100,100)
t.done()