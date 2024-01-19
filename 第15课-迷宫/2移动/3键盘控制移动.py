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

game.listen()#背景监听
#game.onkey(move_up,'Up')#执行内部函数
game.onkeypress(move_up,'Up')#持续移动

t.done()