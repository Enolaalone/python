import turtle
import turtle as t
turtle.tracer(0)
game=t.Screen()
game.title('走迷宫')#取名
game.bgcolor('skyblue')#设置背景颜色
game.setup(800,600)#游戏窗口大小

a=t.Pen()
a.shape('circle')#设置形状
a.fillcolor('white')#设置颜色
a.shapesize(1)#设置大小
a.up()
a.goto(-300,0)
def move(x,y):
    b.up()
    b.goto(x,y)
    b.down()
def line(x1,y1,x2,y2):#划线
     move(x1,y1)
     b.goto(x2,y2)

def move_down():
    a.up()
    a.goto(a.xcor(),a.ycor()-4)
def move_left():
    a.up()
    a.goto(a.xcor()-4,a.ycor())
def move_right():
    a.up()
    a.goto(a.xcor()+4,a.ycor())
b=t.Pen()
b.pensize(15)#设置笔粗细
b.hideturtle()
game.listen()#背景监听
game.onkeypress(move_down,'Down')
game.onkeypress(move_right,'Right')
game.onkeypress(move_left,'Left')

#-------------------------------------------------------

def move_up():
    if a.ycor()<83:#限制范围
        a.up()
        a.goto(a.xcor(),a.ycor()+4)
game.onkeypress(move_up,'Up')#执行内部函数,无括号

line(-400,100,400,100)
line(-400,-100,400,-100)

turtle.tracer(1)
t.done()






