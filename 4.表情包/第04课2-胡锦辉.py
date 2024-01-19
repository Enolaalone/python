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

def face(x, y, r):
    t.speed(0)
    move(x, y - r)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def black(r):
    t.fillcolor("black")
    t.begin_fill()
    t.right(90)
    t.circle(r/8,180)
    t.right(90)
    t.end_fill()

def half_black(r):
    t.fillcolor("black")
    t.begin_fill()
    t.circle(-r/10)
    t.end_fill()

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

def mouth(x, y, r):
    move(-math.sqrt(3) / 3 * r + x, y - r / 3 + r / 6)
    t.right(60)
    t.circle(r * 2 / 3, 120)
    t.right(60)

def mouth1(x,y,r):
    move(x-r/2,y-r/2)
    t.fd(r)


def white_eye(x,y,r):
#----左白眼--------------
    move(x-r/2,y+r/4)
    eye(r)
    #----------黑眼-------------
    half_black(r)

#-------右白眼-----------
    move(x+r/2,y+r/4)
    eye(r)
    half_black(r)


def white_eye2(x, y, r):
    # ----左白眼--------------
    move(x - r / 2, y + r / 4)
    eye(r)
    # ----------黑眼-------------
    move(x - r / 2 - r / 8, y + r / 4)
    black(r)

    # -------右白眼-----------
    move(x + r / 2, y + r / 4)
    eye(r)
    move(x + r / 2 - r / 8, y + r / 4)
    black(r)


#-----------大眼笑--------------
def big_smail(x,y,r):
    face(x, y, r)
    white_eye(x,y,r)
    mouth(x,y,r)

#---------------翻白眼----------
def white_face(x,y,r):
    face(x,y,r)
    white_eye2(x,y,r)
    mouth1(x,y,r)



#--------------哭脸------------------
def sad(x,y,r):
    face(x,y,r)
    eyes(x,y,r)

    move( -math.sqrt(3) / 3 * r +x,y- r / 3+r/6)
    t.right(-60)
    t.circle(-r*2/3,120)
    t.right(-60)

#---------笑脸----------------
def happy(x,y,r):
    face(x,y,r)
    eyes(x,y,r)

    move( -math.sqrt(3) / 3 * r +x,y- r / 3+r/6)
    t.right(60)
    t.circle(r*2/3,120)
    t.right(60)


happy(-100,100,100)
sad(100,100,100)
big_smail(-100,-100,100)
white_face(100,-100,100)





