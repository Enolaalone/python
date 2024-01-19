import time
import turtle as t
import threading
A=[[-300,200,300,200],[-300,200,-300,50],[300,200,300,50],[0,200,0,-75],[-200,200,-200,-75],[200,200,200,-75],
   [-300,-200,300,-200],[-300,-200,-300,-50],[300,-200,300,-50],[-100,-200,-100,75],[100,-200,100,75]]#存放数据
B=[[-388,-280,-32,32],[-280,-220,-180,180],[-220,-180,-180,-92],[-180,-120,-180,180],[-120,-80,92,180],
   [-80,-20,-180,180],[-20,20,-180,-92],[20,80,-180,180],[80,120,92,180],[120,180,-180,180],
   [180,220,-180,-92],[220,280,-180,180],[280,320,-32,32]]


def move_up():  # 向上碰撞反馈
    for i in range(len(B)):
        if (B[i][0] - 1 < a.xcor() < B[i][1] + 1 and B[i][2] - 1 < a.ycor() < B[i][3]):
            a.up()
            a.goto(a.xcor(), a.ycor() + 4)
def move_down():#向下
    for i in range(len(B)):
        if (B[i][0] - 1 < a.xcor() < B[i][1] + 1 and B[i][2] < a.ycor() < B[i][3]+1):
            a.up()
            a.goto(a.xcor(),a.ycor()-4)
def move_left():#向左
    for i in range(len(B)):
        if (B[i][0] < a.xcor() < B[i][1] + 1 and B[i][2]-1 < a.ycor() < B[i][3] + 1):
            a.up()
            a.goto(a.xcor()-4,a.ycor())

def move_right():#向右
    for i in range(len(B)):
        if (B[i][0]-1 < a.xcor() < B[i][1] and B[i][2]-1 < a.ycor() < B[i][3] + 1):
            a.up()
            a.goto(a.xcor()+4,a.ycor())
def up1():
    move_up()
    game.listen()  # 背景监听
    game.onkeypress(move_up, 'Up')  # 执行内部函数,无括号

def down1():
    move_down()
    game.listen()
    game.onkeypress(move_down, 'Down')
def left1():
    move_left()
    game.listen()
    game.onkeypress(move_left, 'Left')
def right1():
    move_right()
    game.listen()
    game.onkeypress(move_right, 'Right')



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
b.pencolor('yellow')
b.pensize(15)#设置笔粗细
b.hideturtle()


#-------------------------------------------
for i in range(11):
    line(A[i][0],A[i][1],A[i][2],A[i][3])
t.tracer(True)
up=threading.Thread(target=up1)
down=threading.Thread(target=down1)
left=threading.Thread(target=left1)
right=threading.Thread(target=right1)
up.start()
down.start()
left.start()
right.start()
t.done()