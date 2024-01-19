import turtle as t
pk=[' 方块A',' 方块2',' 方块3',' 方块4',' 方块5',' 方块6',' 方块7',' 方块8',' 方块9',' 方块10',' 方块J',' 方块Q',' 方块K', \
    ' 方块10',' 方块J',' 方块Q',' 方块K',' 方块J',' 方块Q',' 方块K']#假设一个牌组
#-------移动笔头---------
def move(x,y):#高速移动画笔
    t.speed(0)
    t.hideturtle()  # 隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

def pai1(x,y,pai):#画一张牌，（x,y)牌的位置，pai牌的编号
    move(x,y)
    for i in range(2):
        t.fd(60)
        t.right(90)
        t.fd(90)
        t.right(90)
    t.right(90)
    t.fd(50)
    t.write(pai,font=('黑体',12,'normal'))
    t.fd(40)
    t.left(90)
    t.ht()
t.tracer(False)#瞬间画

x1=-600
y = 100
for i in range(20):#地主牌
    x = 60 * i + x1
    pai1(x,y,pk[i])
x1=-520
y = -200
for i in range(17):#农名牌
    x = 60 * i + x1
    pai1(x,y,pk[i])
x1 = -520
y = -100
for i in range(17):
    x = 60 * i + x1
    pai1(x, y, pk[i])

t.tracer(True)
t.done()