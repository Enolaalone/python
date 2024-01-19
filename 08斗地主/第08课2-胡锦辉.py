import random as r#简化random
import turtle as t
pk=['红\n心\n A','红\n心\n 2弹幕','红\n心\n 3小学算术','红\n心\n 4.进度条','红\n心\n 5','红\n心\n 6','红\n心\n 7','红\n心\n 8', \
    '红\n心\n 9','红\n心\n10','红\n心\n J','红\n心\n Q','红\n心\n K', \
    '梅\n花\n A','梅\n花\n 2弹幕','梅\n花\n 3小学算术','梅\n花\n 4.进度条','梅\n花\n 5','梅\n花\n 6','梅\n花\n 7','梅\n花\n 8', \
    '梅\n花\n 9','梅\n花\n10','梅\n花\n J','梅\n花\n Q','梅\n花\n K', \
    '方\n块\n A','方\n块\n 2弹幕','方\n块\n 3小学算术','方\n块\n 4.进度条','方\n块\n 5','方\n块\n 6','方\n块\n 7','方\n块\n 8', \
    '方\n块\n 9','方\n块\n10','方\n块\n J','方\n块\n Q','方\n块\n K', \
    '黑\n桃\n A','黑\n桃\n 2弹幕','黑\n桃\n 3小学算术','黑\n桃\n 4.进度条','黑\n桃\n 5','黑\n桃\n 6','黑\n桃\n 7','黑\n桃\n 8', \
    '黑\n桃\n 9','黑\n桃\n10','黑\n桃\n J','黑\n桃\n Q','黑\n桃\n K', \
    'j\no\nk\ne','J\nO\nK\nE']#牌库


# -------移动笔头---------
def move(x, y):  # 高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()


def pai1(x, y, pai):  # 画一张牌，（x,y)牌的位置，pai牌的编号
    move(x, y)
    for i in range(2):
        t.fd(60)
        t.right(90)
        t.fd(90)
        t.right(90)
    t.right(90)
    t.fd(60)
    t.write(pai, font=('黑体', 12, 'normal'))
    t.fd(30)
    t.left(90)
    t.ht()


def fa():
    #建立三者牌库
    nm1=[]
    nm2=[]
    dizhu=[]
    #循环依次发牌step3
    for i in range(0, 54, 3):
        a = r.randint(0, 53 - i)  # 抽一个数集合就少一个元素-i
        nm1.append(pk[a])
        del pk[a]
        a = r.randint(0, 52 - i)
        nm2.append(pk[a])
        del pk[a]
        a = r.randint(0, 51 - i)
        dizhu.append(pk[a])
        del pk[a]
    a = r.randint(0, 16)
    dizhu.append(nm1[a])
    del nm1[a]
    a = r.randint(0, 16)
    dizhu.append(nm2[a])
    del nm2[a]

    # 地主牌
    x1 = -600
    y = 100
    for i in range(20):
        x = 60 * i + x1
        pai1(x, y, dizhu[i])
    # 农名1牌
    x1 = -520
    y = -200
    for i in range(17):  # 农名牌
        x = 60 * i + x1
        pai1(x, y, nm1[i])
    # 农名2牌
    x1 = -520
    y = -100
    for i in range(17):
        x = 60 * i + x1
        pai1(x, y, nm2[i])



#-------主程序-----------------
t.tracer(False)
fa()
t.tracer(True)
t.done()