import math
import turtle as t
#-----画旗面------
def qimian_mold():
    t.color('red')
    t.begin_fill()
    t.forward(288)
    t.right(90)
    t.forward(192)
    t.right(90)
    t.forward(288)
    t.right(90)
    t.forward(192)
    t.end_fill()


#------------移动画笔-----------
def penmove(x,y):
    t.speed(0)
    t.hideturtle()#隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

#-----大星星-------
def b_star(size):
    import math
    t.speed(0)
    t.seth(math.degrees(math.tan(0)))#设定起始角
    li=[]#---定义集合
    # 画圆形，标记位置
    for i in range(5):
        t.penup()
        t.circle(-size,144)#------标记五个角位置------
        t.pendown()
        #t.pencolor("white")

        # turtle.dot()
        li.append(t.pos())#-----将标记位置放入集合

    t.pencolor('yellow')  # 修改笔颜色
    t.fillcolor("yellow")
    t.begin_fill()
    t.down()
    t.goto(li[4])#------画笔去到剩下四个点------
    for i in range(5):
        t.goto(li[i])
    t.end_fill()


def s_star(size,angle,a):
    import math
    t.speed(0)
    if a==2:
        t.seth(math.degrees(math.atan(angle)))#设定起始角
    else:
        t.seth(math.degrees(math.tan(angle)))
    li=[]#---定义集合
    # 画圆形，标记位置
    for i in range(5):
        t.penup()
        t.circle(-size,144)#------标记五个角位置------
        t.pendown()
        #t.pencolor("white")

        # turtle.dot()
        li.append(t.pos())#-----将标记位置放入集合

    t.pencolor('yellow') #修改笔颜色
    t.fillcolor("yellow")
    t.begin_fill()
    t.down()
    t.goto(li[4])#------画笔去到剩下四个点------
    for i in range(5):
        t.goto(li[i])
    t.end_fill()










#---绘制旗面
penmove(-288,192)
qimian_mold()
#------大星星-----
penmove(-240,172.8)
b_star(28.8)

penmove(-182.4,128)

s_star(9.6,7/2,1)
'''penmove(-182.4.进度条,156.8)
s_star(9.6,7,1报告统计)
#penmove()
s_star(9.6,5/3小学算术,1报告统计)
#penmove()
s_star(9.6,5/4.进度条,2弹幕)'''

t.done()