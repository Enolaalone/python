import turtle as t
import math

penmove1=[0,0]
hongbu1=[400]#红背景
b_star1=[400,[0,0]]#大星

l_star1=[400,3,5,[0,0]]
l_star2=[400,1,7,[0,0]]

al_star1=[400,2,7,[0,0]]
al_star2=[400,4,5,[0,0]]

def penmove(x, y):  # 高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

def hongbu(w):  #------红布
    t.color('red')
    t.begin_fill()
    for i in range(2):
        t.forward((3 / 2) * w)
        t.left(90)
        t.forward(w)
        t.left(90)
    t.end_fill()


# ---画小星星--------
def little_star(w, a, b, x, y):  # --w旗宽--a/b---tan值----(X,Y)-----右上两颗星星
    l_s = 2 * w / 20 * math.cos(math.pi / 10)
    d1 = 18 + 180 / math.pi * math.atan(a / b)
    dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
    x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
    y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

    penmove(w / 4 + x + x1, w * 3 / 4 + y + y1)  # 移动到位

    t.setheading(d1)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(l_s)
        t.right(144)
    t.end_fill()


def alittle_star(w, a, b, x, y):  # ---右下两颗星星
    l_s = 2 * w / 20 * math.cos(math.pi / 10)
    d1 = 18 - 180 / math.pi * math.atan(a / b)
    dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
    x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
    y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

    penmove(w / 4 + x + x1, w * 3 / 4 + y - y1)

    t.setheading(d1)
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(l_s)
        t.right(144)
    t.end_fill()


# ----------画大星星--------
def b_star(w, x, y):
    penmove(w / 4 + x, y + 9 / 10 * w)
    l_b = 6 * w / 20 * (math.cos(math.pi / 10))
    t.setheading(-72)
    t.pencolor('yellow')  # 修改笔颜色
    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(5):
        t.forward(l_b)
        t.right(144)
    t.end_fill()




penmove(penmove1[0], penmove1[1])
hongbu(hongbu1[0])
b_star(b_star1[0], b_star1[1][0],b_star1[1][1] )

# -------小星星们-------上/下
little_star(l_star1[0], l_star1[1], l_star1[2], l_star1[3][0], l_star1[3][1])
little_star(l_star2[0],l_star2[1],l_star2[2], l_star2[3][0], l_star2[3][1])

alittle_star(al_star1[0], al_star1[1], al_star1[2], al_star1[3][0], al_star1[3][1])
alittle_star(al_star2[0], al_star2[1], al_star2[2], al_star2[3][0], al_star2[3][1])

t.done()