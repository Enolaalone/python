
import turtle

t2=turtle.Pen()
t2.hideturtle()
towers=[[],[],[]]
p=[-400,0,400]
def move_tower(A,C):
    m = towers[A].pop()
    t1.up()
    m.goto(p[A], 100)#从顶端移除
    m.goto(p[C], 100)#从顶端放下
    m.goto(p[C], len(towers[C]) * 20-90)
    towers[C].append(m)  # 将函数'A'对象中的元素移到‘C'对象中
def move(x,y,t):
    t.up()
    t.goto(x,y )
    t.down()
for i in range(20):
    t1 = turtle.Pen()#每次循环都是信画笔，相当是创建了多个鼠标，本质上是移动的turtle*20
    t1.shape('square')#导入鼠标的图案
    t1.shapesize(1,1*i+5)#方块的长宽
    move(0,50-10*i,t1)
    towers[0].append(t1)

move(-400,-100,t2)
t2.goto(-400,100)
move_tower(0,1)

turtle.done()
