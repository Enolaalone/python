import turtle as t
import math
def big_smail(x,y,r):
    #-------移动笔头---------
    def move(x,y):#高速移动画笔
        t.speed(0)
        t.hideturtle()  # 隐藏画笔
        t.pensize(0.2)  # 定义笔大小
        t.penup()
        t.goto(x, y)
        t.pendown()


    def eye(r):
        t.pendown()
        t.fillcolor('white')
        t.begin_fill()
        for i in range(2):
            t.fd(r / 5)
            t.circle(-r / 20, 90)
            t.fd(r / 10)
            t.circle(-r / 20, 90)
            t.fd(r / 5)
        t.end_fill()

    def face(x,y,r):
        t.speed(0)
        move(x,y-r)
        t.fillcolor("yellow")
        t.begin_fill()
        t.circle(r)
        t.end_fill()


    def white_eye(x,y,r):
    #----左白眼--------------
        move(x-r/2,y+r/4)
        eye(r)
        #----------黑眼-------------

        t.fillcolor("black")
        t.begin_fill()
        t.circle(-r/10)
        t.end_fill()
    #-------右白眼-----------
        move(x+r/2,y+r/4)
        eye(r)
        t.fillcolor("black")
        t.begin_fill()
        t.circle(-r / 10)
        t.end_fill()

    def mouth(x,y,r):
        move(-math.sqrt(3) / 3 * r + x, y - r / 3 + r / 6)
        t.right(60)
        t.circle(r * 2 / 3, 120)
        t.right(60)

    face(x, y, r)
    white_eye(x,y,r)
    mouth(x,y,r)

big_smail(0,0,100)