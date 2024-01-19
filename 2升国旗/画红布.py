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

def penmove(x,y):
    t.hideturtle()#隐藏画笔
    t.pensize(0.2)  # 定义笔大小
    t.penup()
    t.goto(x, y)
    t.pendown()
    # print(t.position())


penmove(100,200)









t.done()