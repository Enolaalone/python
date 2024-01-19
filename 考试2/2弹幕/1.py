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

C=['red','green','black','blue','gold','orange','skyblue','pink','purple']

d=turtle.Pen()
d.hideturtle()
e=turtle.Pen()
e.hideturtle()
c=turtle.Pen()
c.hideturtle()
t=turtle.Pen()
t.hideturtle()
f=turtle.Pen()
f.hideturtle()
g=turtle.Pen()
g.hideturtle()
i=turtle.Pen()
i.hideturtle()
j=turtle.Pen()
j.hideturtle()
h=turtle.Pen()
h.hideturtle()
k=turtle.Pen()
k.hideturtle()

def danmu(t):
    y=random.randint(50,400)

    t.up()
    t.goto(-1000, y)
    t.pencolor(C[random.randint(0, len(C) - 1)])
    text=A[random.randint(0, len(A) - 1)]
    size=random.randint(20, 80)
    speed = random.randint(100, 400)
    t.speed(speed)
    while True:
        t.write(text, font=('宋体', size, 'normal'))
        t.fd(speed)
        turtle.tracer(100)
        time.sleep(0.3)
        t.clear()

        if t.xcor() > 550:
            t.goto(-1000,y)
            text = A[random.randint(0, len(A) - 1)]
            size = random.randint(20, 70)
            speed = random.randint(20, 70)

window = turtle.Screen()
t1=threading.Thread(target=danmu,args=(c,))
t2=threading.Thread(target=danmu,args=(d,))
t3=threading.Thread(target=danmu,args=(e,))
t4=threading.Thread(target=danmu,args=(t,))
t5=threading.Thread(target=danmu,args=(f,))
t6=threading.Thread(target=danmu,args=(g,))
t7=threading.Thread(target=danmu,args=(h,))
t8=threading.Thread(target=danmu,args=(i,))
t9=threading.Thread(target=danmu,args=(j,))
t10=threading.Thread(target=danmu,args=(k,))
'''


t11=threading.Thread(target=danmu,args=(l,))
t12=threading.Thread(target=danmu,args=(m,))'''
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
'''


t11.start()'''

window.mainloop()
