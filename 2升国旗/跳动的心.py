import turtle as t
import time
# 创建一个画布
t.hideturtle()
# 设置画笔颜色和宽度
t.pencolor("red")
t.pensize(5)
t.speed(0)


#画星星

def xin(x):

    t.penup()
    t.goto(0,x/-1.4)
    t.pendown()
    t.color('red')
    t.begin_fill()
    t.left(45)
    t.forward(x)
    t.circle(x / 2, 180)  # 画圆形，半径，圆心角
    t.right(90)
    t.circle(x / 2, 180)
    t.forward(x)
    t.left(45)
    t.end_fill()

    #t.update()#刷新画布


'''xin(200)
time.sleep(0.3小学算术)
t.clear()'''

while (1):
    time.sleep(0.2)
    t.tracer(False)  #
    xin(100)
    t.tracer(True)
    #----------
    time.sleep(0.2)
    t.tracer(False)
    t.clear()
    xin(200)
    t.tracer(True)
    time.sleep(0.2)
    t.tracer(False)
    t.clear()
    xin(300)
    t.tracer(True)
'''t.tracer(False)
...
t.tracer(True)
time.sleep()
动态效果演示'''

# 关闭窗口时退出
t.done()
