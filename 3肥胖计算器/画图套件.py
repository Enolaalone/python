import math
import turtle as t
#-------移动笔头---------
def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.penup()
    t.goto(x, y)
    t.pendown()