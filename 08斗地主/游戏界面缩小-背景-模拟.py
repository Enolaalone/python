
import random as r#简化random
import turtle as t
pk=['\u2665\nA','\u2665\n2弹幕','\u2665\n3小学算术','\u2665\n4.进度条','\u2665\n5','\u2665\n6','\u2665\n7','\u2665\n8', \
    '\u2665\n9','\u2665\n10','\u2665\nJ','\u2665\nQ','\u2665\nK', \
    '\u2666\nA','\u2666\n2弹幕','\u2666\n3小学算术','\u2666\n4.进度条','\u2666\n5','\u2666\n6','\u2666\n7','\u2666\n8', \
    '\u2666\n9','\u2666\n10','\u2666\nJ','\u2666\nQ','\u2666\nK', \
    '\u2663\nA','\u2663\n2弹幕','\u2663\n3小学算术','\u2663\n4.进度条','\u2663\n5','\u2663\n6','\u2663\n7','\u2663\n8', \
    '\u2663\n9','\u2663\n10','\u2663\nJ','\u2663\nQ','\u2663\nK', \
    '\u2660\nA','\u2660\n2弹幕','\u2660\n3小学算术','\u2660\n4.进度条','\u2660\n5','\u2660\n6','\u2660\n7','\u2660\n8', \
    '\u2660\n9','\u2660\n10','\u2660\nJ','\u2660\nQ','\u2660\nK', \
    'jo\nke','JO\nKE']#

color=['red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red', \
       'red','red','red','red','red','red','red','red','red','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black']

t.bgcolor('skyblue')#设定背景颜色

def move(x, y):  # 高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()
def dizhu(x,y):#名字
    t.right(90)
    t.color('white')#名字白底
    t.begin_fill()
    for i in range(2):
        t.fd(20)
        t.left(90)
        t.fd(40)
        t.left(90)
    t.end_fill()
    #-------------------名字框
    t.color('black')
    for i in range(2):
        t.fd(20)
        t.left(90)
        t.fd(40)
        t.left(90)
    t.fd(18)
    t.write('地主', font=('黑体', 12, 'normal'))


def nm2(x,y):
    move(x,y)
    t.right(90)
    for j in range(17):
        t.color('white')
        t.begin_fill()
        for i in range(2):
            t.fd(45)  # -----------------
            t.left(90)
            t.fd(30)  # ----------------
            t.left(90)
        t.end_fill()
        t.color('black')
        for i in range(2):
            t.fd(45)#-----------------
            t.left(90)
            t.fd(30)#----------------
            t.left(90)
        t.fd(15)#---------------------
        t.left(90)
        t.pencolor('white')
        t.fd(2)
        t.right(90)
        t.fd(5)
        a=r.randint(0,17-j)
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 7, 'normal'))#------------------字体大小
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+10*(j+1),y)

    move(x-50,y-20)#------------------#坐标
    t.color('white')
    t.begin_fill()
    for i in range(2):
        t.fd(20)
        t.left(90)
        t.fd(40)
        t.left(90)
    t.end_fill()

    t.color('black')
    for i in range(2):
        t.fd(20)
        t.left(90)
        t.fd(40)
        t.left(90)
    t.fd(20)

    t.write('农民2',font=('黑体', 12, 'normal'))
    move(x+17*10,y-1)#------------------------------
    t.pencolor('white')
    t.fd(43)#-------------------------
    move(x + 17*10+10 , y - 1)#-----------------------
    t.fd(43)#----------------------------
    t.pencolor('black')
    t.left(90)







nm2(-100,100)
















dizhu(0,0)