import turtle,time,threading
def p(x,y):#点击后返回坐标，使k=1报告统计
    global k
    k=1

t1=turtle.Pen()#写字
t2=turtle.Pen()#写数字
t1.up()
t2.up()
t1.hideturtle()
t2.hideturtle()
t1.pencolor('red')
#----------------标题--------------------
t1.goto(-330,200)
t1.write('抢10大比拼',font=('宋体', 100, 'normal'))

#--------------------------事件------------------
star=0
add=0.02
k=0 #global量

turtle.onscreenclick(p)
while star<=11:
    turtle.tracer(False)
    star+=add
    t2.goto(-160,-100)
    t2.write('{:.2f}'.format(star),font=('宋体',100,'normal'))
    turtle.tracer(True)
    time.sleep(0.3)

    turtle.tracer(0)
    t2.clear()
    turtle.tracer(1)
    if k==1:
        time.sleep(1)
        if (star==10.00):
            t1.clear()
            t2.clear()
            t1.goto(-250, 0)
            t1.write('恭喜成功', font=('宋体', 100, 'normal'))
            break
        else:
            t1.clear()
            t2.clear()
            t1.goto(-250, 0)
            t1.write(' 苦呀西！\n游戏失败', font=('宋体', 100, 'normal'))
            break

turtle.done()