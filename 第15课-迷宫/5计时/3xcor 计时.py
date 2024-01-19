import time
import turtle as t
import threading#------导入时间线程，让移动不卡顿
game=t.Screen()
game.title('走迷宫')#取名
game.bgcolor('skyblue')#设置背景颜色
game.setup(800,600)#游戏窗口大小
start_time = time.time()# 记录开始时间
a=t.Pen()
a.shape('circle')#设置形状
a.fillcolor('white')#设置颜色
a.shapesize(1)#设置大小

def move_up():
    a.up()
    a.goto(a.xcor(),a.ycor()+4)
    print(a.xcor(),a.ycor())
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
#========================================
def time_1():#计时和终点线程
    while(1):
        time.sleep(0.25)#人的视觉暂停0．05至0．2秒
        c.clear()
        end_time=time.time()-0.25
        c.write(f'耗时：{end_time-star_time:.2f}',font=('宋体',20,'normal'))
        if a.xcor()>300 and a.ycor()<32:
            break
        else:
            continue

#=================================================================
t.tracer(0)
star_time=time.time()
c=t.Pen()
c.pencolor('red')
c.up()
c.goto(-70,250)
c.hideturtle()
t.tracer(1)
game.listen()  # 背景监听
game.onkeypress(move_up, 'Up')  # 执行内部函数,无括号
game.onkeypress(move_down, 'Down')
game.onkeypress(move_right, 'Right')
game.onkeypress(move_left, 'Left')


t1 = threading.Thread(target=time_1)#时间线程
t1.start()

t.done()


