
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

#------画直方图-------
t.pencolor("red")
t.pensize(1)
move(x0,y0)
for i in range(len(ls)):#确定柱状图个数
    x=x0+(i+1)*50
    y=y0
    move(x,y)#确定直方图起始点
    for j in range(ls[i][1]):#确定宽度
        t.seth(90)
        t.fd(ls[i][0])
        x=x+1
        move(x,y)
t.done()














