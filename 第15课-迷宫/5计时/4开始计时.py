import time
import turtle as t
def start(x,y):
    global k
    k=1
k=0


game=t.Screen()
game.title('走迷宫')#取名
game.bgcolor('skyblue')#设置背景颜色
game.setup(800,600)#游戏窗口大小

t.hideturtle()
t.up()
t.goto(-200,0)
t.color('red')
t.onscreenclick(start)
while(True):
    t.write('点击开始游戏',font=('宋体',50,'normal'))
    time.sleep(1)
    t.clear()
    if k==1:
        break
    else:
        continue
t.done()