import turtle as t
import math

def move(x,y):
    t.pu()
    t.goto(x,y)
    t.pd()

def face(x,y):
    t.color('yellow')
    move(x,y-100)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def eye_1(x,y):
    t.seth(0)
    move(x,y)
    t.color('black')
    for i in range(2):
        t.fd(20)
        t.circle(5,90)
        t.fd(10)
        t.circle(5,90)
        t.fd(20)
    move(x-10,y+20)
    t.seth(-90)
    t.begin_fill()
    t.circle(10,180)
    t.end_fill()

def eye_2(x,y):
    t.seth(0)
    move(x,y)
    t.color('black')
    for i in range(2):
        t.fd(20)
        t.circle(5,90)
        t.fd(10)
        t.circle(5,90)
        t.fd(20)

    t.begin_fill()
    t.circle(10)
    t.end_fill()

#------------------------------------------
def mouth_2(x,y):
    move(x-50,y)
    t.seth(-90)
    t.circle(50,180)

def mouth_1(x,y):
    move(x-40,y-50)
    t.seth(0)
    t.fd(80)
#-------------------------------------------

def emoji_1(x,y):
    face(x,y)
    eye_1(x-35,y+25)
    eye_1(x+35,y+25)
    mouth_1(x,y)


def emoji_2(x,y):
    face(x,y)
    eye_2(x-35,y+25)
    eye_2(x+35,y+25)
    mouth_1(x,y)

def emoji_3(x,y):
    face(x,y)
    eye_2(x-35,y+25)
    eye_2(x+35,y+25)
    mouth_2(x,y)

#-------------------------------------------
def American(x,y):
    t.seth(180)
    for i in range(4):
        move(x,y+(100-20*i))
        if i==0:
            t.color('red')
        if i==1:
            t.color('white')
        if i==2:
            t.color('red')
        if i==3:
            t.color('blue')
        t.begin_fill()
        t.circle(100-20*i)
        t.end_fill()
    t.color('white')
    t.seth(-72)
    t.begin_fill()
    for i in range(5):
        t.fd(2*40*math.cos(15*math.pi/180))
        t.right(144)
    t.end_fill()

t.tracer(0)

emoji_1(100,100)
emoji_2(-100,100)
emoji_3(-100,-100)
American(100,-100)

t.tracer(1)
t.done()

