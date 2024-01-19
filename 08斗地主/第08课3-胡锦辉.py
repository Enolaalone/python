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
    'jo\nke','JO\nKE']#牌库

color=['red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red','red', \
       'red','red','red','red','red','red','red','red','red','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black','black','black', \
       'black','black','black','black','black','black','black','black','black','black']#颜色库


# -------移动笔头---------
def move(x, y):  # 高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

def dizhu(x,y):
    move(x,y)
    t.right(90)
    #随机取牌，并画牌
    for j in range(20):#地主20张
        #画牌框
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
        #写牌花色
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
        #从牌库，色库删除索取的颜色
        del pk[a]
        del color[a]
        move(x+20*(j+1),y)
    #左侧写名字
    move(x-50,y-30)
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
    t.write('地主',font=('黑体', 12, 'normal'))
    #删去第20张牌上多余的线
    move(x+20*20,y-1)
    t.pencolor('white'  )
    t.fd(88)
    move(x + 20* 20+20 , y - 1)
    t.fd(88)
    t.pencolor('black'  )
    t.left(90)

def nm1(x,y):#画牌方法同地主
    move(x,y)
    t.right(90)
    for j in range(17):#农名17张
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
        a=r.randint(0,33-j)#地主取牌后还有34张
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 13, 'normal'))
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+20*(j+1),y)

    move(x-50,y-30)
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

    move(x+17*20,y-1)
    t.pencolor('white'  )
    t.fd(88)
    move(x + 17* 20+20 , y - 1)
    t.fd(88)
    t.pencolor('black'  )
    t.left(90)


def nm2(x,y):#农民2
    move(x,y)
    t.right(90)
    for j in range(17):
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
        a=r.randint(0,16-j)#最后还有17张
        t.pencolor(color[a])
        t.write( pk[a],font=('宋体', 13, 'normal'))
        t.pencolor('black')
        del pk[a]
        del color[a]
        move(x+20*(j+1),y)

    move(x-50,y-30)
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

    move(x+17*20,y-1)
    t.pencolor('white'  )
    t.fd(88)
    move(x + 17* 20+20 , y - 1)
    t.fd(88)
    t.pencolor('black'  )
    t.left(90)

#---------主程序----------------
t.tracer(False)#瞬间显示
dizhu(-200,200)
nm1(-150,0)
nm2(-150,-100)
t.tracer(True)
t.done()