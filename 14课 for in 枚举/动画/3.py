import random
import turtle
import time
he=[[],['长江'],[]]
p=[[-550,200],[-550,0],[-550,-200],[550,200],[550,0],[550,-200]]#坐标


turtle.register_shape('lang.gif')#注册turtle
turtle.register_shape('yang.gif')
turtle.register_shape('cai.gif')
turtle.register_shape('chuan.gif')
turtle.register_shape('he.gif')
a=turtle.Pen()
b=turtle.Pen()
c=turtle.Pen()
d=turtle.Pen()
e=turtle.Pen()
e.shape('he.gif')
a.shape('lang.gif')
b.shape('cai.gif')
c.shape('yang.gif')
d.shape('chuan.gif')


a.up()
b.up()
c.up()
d.up()

A=[a,b,c]
for i in range(len(A)):
    e=random.randint(0,len(A)-1)
    he[0].append(A.pop(e))



turtle.tracer(0)

a.goto(p[0][0],p[0][1])
b.goto(p[1][0],p[1][1])
c.goto(p[2][0],p[2][1])
turtle.tracer(1)

d.goto(-500, 0)
time.sleep(1)
while (True):
    n= random.randint(0, len(he[0]) - 1)
    m= he[0].pop(n)
    if ((c in he[0] )and (a in he[0])) or ((c in he[0] )and(b in he[0] ) ):#让羊先过河
        he[0].append(m)
        continue
    else:
         he[2].append(m)#随机将【0】中元素移到【2弹幕】中
         m.goto(-550, 0)
         for i in range(100):
             m.seth(0)
             m.fd(11)
             d.seth(0)
             d.fd(10)
         break
print(he)
d.goto(-500, 0)

#----------------------
while (1):#之后让计算机随机移动一个元素，满足狼和菜在右岸
    he[2].append(he[0].pop(0))
    he[2][1].goto(-550, 0)
    for i in range(100):
        he[2][1].seth(0)
        he[2][1].fd(11)
        d.seth(0)
        d.fd(10)


    if ((c in he[0] )and (a in he[0])) or ((c in he[0] )and(b in he[0] ) ) or \
        ((c in he[2]) and (a in he[2])) or ((c in he[2]) and (b in he[2])) or \
            ((a in he[0]) and (b in he[0] ) ):
        he[0].append(he[2].pop(0))
        for i in range(100):
            he[0][1].seth(-180)
            he[0][1].fd(11)
            d.seth(-180)
            d.fd(10)

    else:#满足上述条件后，只要把羊从左岸到右岸即可
        he[2].append(he[0].pop(0))
        d.goto(-500, 0)
        for i in range(100):
            he[2][2].seth(0)
            he[2][2].fd(11)
            d.seth(0)
            d.fd(10)
        break

turtle.done()