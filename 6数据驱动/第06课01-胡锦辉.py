import turtle as t
tri1=[[-300,150],[-125,-125],[-50,-50]]
tri2=[[0,0],[100,50],[-300,150]]
tri3=[[-85,-85],[-50,-50],[-30,-125]]
line1=[[0,0],[-30,-125]]
circle1=[250,200]

def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(5)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()
def tri(x1,y1,x2,y2,x3,y3):#画三角形
    move(x1,y1)
    t.color('black','blue')
    t.begin_fill()
    t.goto(x2, y2)
    t.goto(x3, y3)
    t.goto(x1,y1)
    t.end_fill()

def line(x1,y1,x2,y2):#画线
    t.color('black')
    move(x1,y1)
    t.goto(x2,y2)

def cir_cle(x,y,r,color):#画太阳
    move(x,y)
    t.color(color)
    t.begin_fill()
    t.circle(r)
    t.end_fill()


tri(tri1[0][0],tri1[0][1],tri1[1][0],tri1[1][1],tri1[2][0],tri1[2][1])
tri(tri2[0][0],tri2[0][1],tri2[1][0],tri2[1][1],tri2[2][0],tri2[2][1])
tri(tri3[0][0],tri3[0][1],tri3[1][0],tri3[1][1],tri3[2][0],tri3[2][1])
line(line1[0][0],line1[0][1],line1[1][0],line1[1][1])
cir_cle(circle1[0],circle1[1],30,'red')
t.done()