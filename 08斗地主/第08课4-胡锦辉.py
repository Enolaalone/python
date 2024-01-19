import random as r#简化random
import turtle as t
pk=['\u2665\nA','\u2665\n2','\u2665\n3','\u2665\n4.','\u2665\n5','\u2665\n6','\u2665\n7','\u2665\n8', \
    '\u2665\n9','\u2665\n10','\u2665\nJ','\u2665\nQ','\u2665\nK', \
    '\u2666\nA','\u2666\n2','\u2666\n3','\u2666\n4.','\u2666\n5','\u2666\n6','\u2666\n7','\u2666\n8', \
    '\u2666\n9','\u2666\n10','\u2666\nJ','\u2666\nQ','\u2666\nK', \
    '\u2663\nA','\u2663\n2','\u2663\n3','\u2663\n4.','\u2663\n5','\u2663\n6','\u2663\n7','\u2663\n8', \
    '\u2663\n9','\u2663\n10','\u2663\nJ','\u2663\nQ','\u2663\nK', \
    '\u2660\nA','\u2660\n2','\u2660\n3','\u2660\n4.','\u2660\n5','\u2660\n6','\u2660\n7','\u2660\n8', \
    '\u2660\n9','\u2660\n10','\u2660\nJ','\u2660\nQ','\u2660\nK', \
    'jo\nke','JO\nKE']#牌库


color=['red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red', \
       'red','red','red','red','red','red','red','red','red','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black']#色库和牌库一一对应
t.bgcolor('skyblue')
# -------移动笔头---------
def move(x, y):  # 高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

def anniu(x,y):#画名字框
    move(x , y)
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
def dizhu(x,y):
    move(x,y)
    t.right(90)
    for j in range(20):
        t.color('white')
        t.begin_fill()
        for i in range(2):
            t.fd(90)
            t.left(90)
            t.fd(60)
            t.left(90)
        t.end_fill()
        t.color('black')
        for i in range(2):
            t.fd(90)
            t.left(90)
            t.fd(60)
            t.left(90)

        t.fd(30)
        t.left(90)
        t.pencolor('white')
        t.fd(3)
        t.right(90)
        t.fd(5)
        a=r.randint(0,53-j)
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 13, 'normal'))
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+20*(j+1),y)
    anniu(x-50,y-30)
    t.write('地主',font=('黑体', 12, 'normal'))
    anniu(x - 50, y -60)
    t.write('退出', font=('黑体', 12, 'normal'))
    anniu(x+180,y+30)
    t.write('开始', font=('黑体', 12, 'normal'))
    move(x+20*20,y-1)
    t.pencolor('white'  )
    t.fd(88)
    move(x + 20* 20+20 , y - 1)
    t.fd(88)
    t.pencolor('black'  )
    t.left(90)

def nm1(x,y):
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
        a=r.randint(0,33-j)
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 7, 'normal'))#------------------字体大小
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+10*(j+1),y)
#写名字-----------------------------------
    move(x+20,y+30)#------------------#坐标
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
    t.write('农民1',font=('黑体', 12, 'normal'))
#----------------------删去牌上多余的线
    move(x+17*10,y-1)#------------------------------
    t.pencolor('white')
    t.fd(43)#-------------------------
    move(x + 17*10+10 , y - 1)#-----------------------
    t.fd(43)#----------------------------
    t.pencolor('black')
    t.left(90)


def nm2(x,y):#同农民1---------------------表示数据改变
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
        a=r.randint(0,16-j)
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 7, 'normal'))#------------------字体大小
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+10*(j+1),y)

    move(x+20,y+30)#------------------#坐标
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


t.tracer(False)
#欢乐斗地主背景板
t.color('skyblue')
t.right(90)
move(-320,200)
for i in range(2):
    t.fd(300)
    t.left(90)
    t.fd(660)
    t.left(90)
t.fd(200)
t.color('black')
t.write('欢乐斗地主', font=('黑体', 100, 'normal'))
t.left(90)

#分别发牌
dizhu(-220,-200)
nm1(-400,300)
nm2(220,300)
t.tracer(True)
t.done()