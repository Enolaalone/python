import math
import turtle as t
#-------移动笔头---------
def penmove(x,y):#高速移动画笔
    t.speed(1)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

#---画小星星--------
def little_star(w,a,b,x,y):#--w旗宽--a/b---tan值----(X,Y)
    l_s = 2 * w / 20 * math.cos(math.pi / 10)
    d1 = 18 +180/math.pi*math.atan(a / b)
    dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
    x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
    y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

    penmove(w/4+x+x1,w*3/4+y+y1)#移动到位

    t.setheading(d1)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(l_s)
        t.right(144)
    t.end_fill()


def alittle_star(w,a,b,x,y):#--w旗宽--a/b---tan值----(X,Y)
    l_s = 2 * w / 20 * math.cos(math.pi / 10)
    d1 = -18 -180/math.pi*math.atan(a / b)
    dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
    x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
    y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

    penmove(w/4+x+x1,w*3/4+y-y1)
    t.setheading(d1)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(l_s)
        t.right(144)
    t.end_fill()
#------绘制红布------------
def wuxinghongqi_mold(w,x,y):
    penmove(x, y)

    t.color('red')
    t.begin_fill()
    for i in range(2):
        t.forward((3/2)*w)
        t.left(90)
        t.forward(w)
        t.left(90)
    t.end_fill()


#----------画大星星--------

    penmove(w/4+x,y+9/10*w)

    l_b=6*w/20*(math.cos(math.pi/10))
    t.setheading(-72)
    t.pencolor('yellow')  # 修改笔颜色
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):

        t.forward(l_b)
        t.right(144)
    t.end_fill()
#-------小星星们-------
    little_star(w,3,5,x,y)
    little_star(w, 1, 7, x, y)
    alittle_star(w, 2, 7, x, y)
    alittle_star(w, 4, 5, x, y)

#---一笔化成----->< >< ><
wuxinghongqi_mold(400,0,0)#--w确定了国旗的宽--(X,Y)是国旗左下角位置
t.done()