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
t.dot(20,'black')
def m_circle(x,y,r,color):
    move(x,y-r)
    t.fillcolor(f'{color}')#填入颜色
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def star(x,y,r,color):
    move(x,y)
    t.right(72)
    t.fillcolor(f'{color}')
    t.begin_fill()
    for i in range(5):
        t.forward(2*r*math.cos(math.pi/180))#cos()中的是弧度：n*math.pi/180----转换
        t.right(144)
    t.end_fill()
    t.right(-72)


def face(x, y, r):
    t.speed(0)
    move(x, y - r)
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def g_eye(x,y,r):
    move(x+r/3,math.sqrt(3)/3*r+y-r/6)
    t.circle(r/6)

    move(x+r/3+(r/(6*math.sqrt(2))/2),math.sqrt(3)/3*r+y-r/(6*math.sqrt(2)))
    t.fillcolor('black')
    t.begin_fill()
    t.circle(r/12)
    t.end_fill()
#-----------------------------------
    move(x - r / 3, math.sqrt(3) / 3 * r + y - r / 6)
    t.circle(r / 6)

    move(x - r / 3 - (r / (6 * math.sqrt(2)) / 2), math.sqrt(3) / 3 * r + y)
    t.fillcolor('black')
    t.begin_fill()
    t.circle(r / 12)
    t.end_fill()

def mouth(x,y,r):
    move(-math.sqrt(3) / 3 * r + x, y - r / 3 + r / 6)
    t.right(60)
    t.circle(r * 2 / 3, 120)
    t.right(60)

def happy3(x,y,r):
    face(x,y,r)
    g_eye(x, y, r)
    mouth(x, y, r)


#---美国队长----------------
t.pencolor('white')
m_circle(0,0,200,'red')
m_circle(0,0,170,'white')
m_circle(0,0,140,'red')
m_circle(0,0,110,'blue')

move(0,110)
star(0,0,110,'white')


#-----搞笑美国队长-----------
m_circle(0,400,200,'red')
m_circle(0,400,170,'white')
m_circle(0,400,140,'red')
m_circle(0,400,110,'blue')
t.pencolor('white')
happy3(0,400,110)

t.done()













