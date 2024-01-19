import turtle as t
ls=[[69,15],[292,10],[33,8],[131,10],[61,5],[254,10],[100,15],[80,25] ]
X_len=500
Y_len=300
x0=-200
y0=-100

def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.penup()
    t.goto(x, y)
    t.pendown()
#------建系------

move(x0,y0)
t.fd(X_len)
move(x0,y0)
t.seth(90)
t.fd(Y_len)
t.seth(0)
#------画直方图-------
t.pencolor("red")
t.pensize(1)
move(x0,y0)
for j in range(len(ls)):
    move(50*(j+1)+x0,y0)
    t.color('red')
    t.begin_fill()
    for i in range(2):
        t.fd(ls[j][1])
        t.left(90)
        t.fd(ls[j][0])
        t.left(90)
    t.end_fill()

t.done()