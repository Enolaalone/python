import turtle
import random
import time
import threading

with open('弹幕.txt','r',encoding='utf-8') as f:
    a=f.readlines()
    print(a)
    A=[]
    for i in a:
        b=i.strip('\n')
        A.append(b)

    num=random.randint(0,len(A))
    print(num)

C=['red','green','black','blue','gold','orange','purple']

d=turtle.Pen()
e=turtle.Pen()
c=turtle.Pen()

danmu=[]

for i in range(20):
    text = A[random.randint(0, len(A) - 1)]
    size = random.randint(20, 70)
    speed1 = random.randint(10, 30)
    y = random.randint(0, 400)

    t=turtle.Turtle()
    t.up()
    t.hideturtle()
    t.goto(-1500, y)
    t.pencolor(C[random.randint(0, len(C) - 1)])
    t.speed(speed1)

    danmu.append(t)












#t.done()