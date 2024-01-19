import turtle as t
t.speed(100)

#------------------星星模块----------------
def star(size):
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(-144)
    t.end_fill()


#----------红布------------------
def L_mold():
    t.forward(600)
    t.right(90)
    t.forward(400)
    t.right(90)



#------------移动画笔-----------
def penmove(x,y):#该移动方法不改变画笔方向
    t.hideturtle()#隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()

penmove(-300,200)
#----------上色--------------

t.color('red')
t.begin_fill()
L_mold()
L_mold()
t.end_fill()

#-------大星星-------
penmove(-257,120)
star(120)
#--------小星星--------
penmove(-122,150)
t.left(45)
star(40)
#---------小星星2-------
penmove(-60,96)
t.left(60)
star(40)
#---------小星星3-------
penmove(-72,40)
t.right(32)
star(40)
#---------小星星4--------
penmove(-117,0)
t.right(30)
star(40)


t.done()