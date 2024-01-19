import time
import turtle as t
A=[[-300,200,300,200],[-300,200,-300,50],[300,200,300,50],[0,200,0,-75],[-200,200,-200,-75],[200,200,200,-75],
   [-300,-200,300,-200],[-300,-200,-300,-50],[300,-200,300,-50],[-100,-200,-100,75],[100,-200,100,75]]#存放数据

def move_up():
    a.up()
    a.goto(a.xcor(),a.ycor()+4)
    print(a.xcor(), a.ycor())
def move_down():
    a.up()
    a.goto(a.xcor(),a.ycor()-4)
    print(a.xcor(), a.ycor())
def move_left():
    a.up()
    a.goto(a.xcor()-4,a.ycor())
    print(a.xcor(), a.ycor())
def move_right():
    a.up()
    a.goto(a.xcor()+4,a.ycor())
    print(a.xcor(), a.ycor())

def move(x,y):
    b.up()
    b.goto(x,y)
    b.down()
def line(x1,y1,x2,y2):#划线
     move(x1,y1)
     b.goto(x2,y2)
t.tracer(False)
game=t.Screen()#导入屏幕
game.title('走迷宫')#取名
game.bgcolor('black')#设置背景颜色
game.setup(800,600)#游戏窗口大小

a=t.Pen()
a.shape('circle')#设置形状
a.fillcolor('blue')#设置颜色
a.shapesize(1)#设置大小
a.up()
a.goto(-300,0)
#第二只画笔
b=t.Pen()
b.pensize(15)#设置笔粗细
b.color('yellow')
b.hideturtle()
#-------------------------------------------

game.listen()#背景监听
game.onkeypress(move_up,'Up')#执行内部函数,无括号
game.onkeypress(move_down,'Down')
game.onkeypress(move_right,'Right')
game.onkeypress(move_left,'Left')


for i in range(11):
    line(A[i][0],A[i][1],A[i][2],A[i][3])

t.tracer(True)
t.done()