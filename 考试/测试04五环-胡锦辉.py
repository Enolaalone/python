import turtle as t

huan1=[[-280,180,120,'blue'],[0,180,120,'black'],[280,180,120,'red'],[150,60,120,'green'],[-150,60,120,'yellow']]
huan2=[[0,180,120,-20,'black'],[280,180,120,-20,'red'],[0,420,-120,100,'black'],[-280,420,-120,100,'blue']]


def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.width(20)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

def huan(x,y,r,color):#画五环
    move(x,y)
    t.pencolor(color)
    t.circle(r)

def huan_1(x,y,r,dg,color):
    move(x,y)
    t.pencolor(color)
    t.circle(r,dg)
    t.seth(0)


for i in range(5):
    huan(huan1[i][0],huan1[i][1],huan1[i][2],huan1[i][3])
for j in range(4):
    huan_1(huan2[j][0],huan2[j][1],huan2[j][2],huan2[j][3],huan2[j][4])

t.done()

