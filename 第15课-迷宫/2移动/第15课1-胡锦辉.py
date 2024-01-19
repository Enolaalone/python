import turtle as t
import time
game=t.Screen()
game.title('走迷宫')#取名
game.bgcolor('skyblue')#设置背景颜色
game.setup(800,600)#游戏窗口大小

a=t.Pen()
a.shape('circle')#设置形状
a.fillcolor('white')#设置颜色
a.shapesize(1)#设置大小
#-------------------------------------------
a.up()#无痕
while(True):
        a.goto(a.xcor()+5,a.ycor()+5)
        time.sleep(0.1)

t.done()