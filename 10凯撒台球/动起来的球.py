import turtle as t
import time
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
s=0.01

'''for i in range(100):
    if t.xcor()<100:

        t.hideturtle()
        t.tracer(False)
        move(-200+10*i,0)
        t.color('red')
        t.begin_fill()
        t.circle(40)
        t.end_fill()
        t.update()
        time.sleep(s + 0.001 * i)
        t.clear()
    else:
        move(-200,0)'''

while True:

    move(-560, 0)
    # 隐藏箭头回到左侧
    while t.ycor() < 10:  # 屏幕右侧的 x 坐标
        for i in range(20):
            t.seth(45)
            time.sleep(s + 0.01 * i)
            t.hideturtle()
            t.penup()
            t.fd(3 * i)
            t.pendown()
            t.tracer(False)
            t.color('red')
            t.begin_fill()
            t.circle(15)
            t.end_fill()
            t.update()

            t.clear()


