import time
import turtle as t
A=[[-300,200,300,200],[-300,200,-300,50],[300,200,300,50],[0,200,0,-75],[-200,200,-200,-75],[200,200,200,-75],
   [-300,-200,300,-200],[-300,-200,-300,-50],[300,-200,300,-50],[-100,-200,-100,75],[100,-200,100,75]]#存放数据

def move_up():#向上碰撞反馈
    if (((-400<=a.xcor()<= -284 and a.ycor()<32) or (-284<=a.xcor()<= -216 and a.ycor()<184) or
        (-216<=a.xcor()<= -184 and a.ycor()< -92) or(-184<=a.xcor()<= -16 and a.ycor()<184) or
            (-16<=a.xcor()<=16 and a.ycor()< -92)or(16<=a.xcor()<=184 and a.ycor()<184) or
        (184<=a.xcor()<=216 and a.ycor()< -92) or (216<=a.xcor()<=284 and a.ycor()<184)) or
            (284<=a.xcor()<=400 and a.ycor()<32)):
        a.up()
        a.goto(a.xcor(),a.ycor()+4)
        print(a.xcor(),a.ycor())
def move_down():#向下
    if ((-400<=a.xcor()<= -284 and a.ycor()> -32) or (-284<=a.xcor()<= -184 and a.ycor()> -184)
            or(-184<=a.xcor()<= -116 and a.ycor()> -184)or(-116<=a.xcor()<=-84 and a.ycor()>88)or
            (-84<=a.xcor()<= 84 and a.ycor()> -184) or(84<=a.xcor()<=116 and a.ycor()>88) or
            (116<=a.xcor()<=284 and a.ycor()> -184) or(284<=a.xcor()<=400 and a.ycor()> -32)):
        a.up()
        a.goto(a.xcor(),a.ycor()-4)
        print(a.xcor(), a.ycor())
def move_left():#向左
    if((-400<=a.xcor()<= -284 and -32<=a.ycor()<=32) or (-280<=a.xcor()<=-212)or (-212<=a.xcor()<= -180 and a.ycor()< -88) or
       (-180<=a.xcor()<= -116) or (-116<=a.xcor()<=-80 and a.ycor()>= 92)or (-80<=a.xcor()<=-16) or
       (-16<=a.xcor()<=20 and a.ycor()<= -92) or(20<=a.xcor()<=84)or(84<=a.xcor()<=120 and a.ycor()>=92)or
       (120<=a.xcor()<=184) or(184 <= a.xcor() <= 216 and a.ycor() <=-92)or (220<=a.xcor()<=400)) :
        a.up()
        a.goto(a.xcor()-4,a.ycor())
        print(a.xcor(), a.ycor())
def move_right():#向右
    if ((-400<=a.xcor()<= -218) or (-218<=a.xcor()<= -184 and a.ycor()< -88) or (-184<=a.xcor()<= -120) or
            (-120<=a.xcor()<=-88 and a.ycor()> 88) or (-88<=a.xcor()<=-20) or (-20<=a.xcor()<=12 and a.ycor()< -88) or
            (12<=a.xcor()<=80) or (80<=a.xcor()<=112 and a.ycor()>88) or  (112<=a.xcor()<=180) or
            (180 <= a.xcor() <= 212 and a.ycor() < -88) or (212<=a.xcor()<=280)) or (280<=a.xcor()<= 312 and -32<a.ycor()<32):
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
b.pencolor('yellow')
b.pensize(15)#设置笔粗细
b.hideturtle()

game.listen()#背景监听
game.onkeypress(move_up,'Up')#执行内部函数,无括号
game.onkeypress(move_down,'Down')
game.onkeypress(move_right,'Right')
game.onkeypress(move_left,'Left')
#-------------------------------------------
for i in range(11):
    line(A[i][0],A[i][1],A[i][2],A[i][3])
t.tracer(True)

t.done()