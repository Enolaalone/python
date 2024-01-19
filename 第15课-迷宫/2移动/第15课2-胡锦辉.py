import time
import turtle as t
game=t.Screen()
game.title('走迷宫')#取名
game.bgcolor('skyblue')#设置背景颜色
game.setup(800,600)#游戏窗口大小

a=t.Pen()
a.shape('circle')#设置形状
a.fillcolor('white')#设置颜色
a.shapesize(1)#设置大小
#-------------------------------------------
def move_up():
    a.up()
    a.goto(a.xcor(),a.ycor()+4)
def move_down():
    a.up()
    a.goto(a.xcor(),a.ycor()-4)
def move_left():
    a.up()
    a.goto(a.xcor()-4,a.ycor())
def move_right():
    a.up()
    a.goto(a.xcor()+4,a.ycor())
game.listen()#背景监听
game.onkeypress(move_up,'Up')#执行内部函数,无括号
game.onkeypress(move_down,'Down')
game.onkeypress(move_right,'Right')
game.onkeypress(move_left,'Left')

t.done()