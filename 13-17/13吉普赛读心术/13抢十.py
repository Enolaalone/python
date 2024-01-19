import turtle,time,Data1
def p(x,y):
    global k
    k=1

t1=turtle.Pen()
t2=turtle.Turtle()
t1.pu()
t2.pu()
t1.hideturtle()
t2.hideturtle()
t1.color('red')

t1.goto(Data1.move[0][0],Data1.move[0][1])
t1.write('抢10大比拼',font=('宋体',100,"normal"))

star=0
add=0.02
k=0
turtle.onscreenclick(p)
while star<=11:
    turtle.tracer(0)
    star+=add
    t2.goto(Data1.move[1][0],Data1.move[1][1])
    t2.write(f'{star:.2f}',font=('宋体',100,"normal"))
    turtle.tracer(1)

    time.sleep(0.3)
    turtle.tracer(0)
    t2.clear()
    turtle.tracer(1)
    if k==1:
        time.sleep(0.1)
        if star==10.00:
            t1.clear()
            t2.clear()
            t1.goto(Data1.move[2][0],Data1.move[2][1])
            t1.write('游戏成功',font=('宋体',100,"normal"))
            break

        else:
            t1.clear()
            t2.clear()
            t1.goto(Data1.move[2][0],Data1.move[2][1])
            t1.write('游戏失败',font=('宋体',100,"normal"))
            break
turtle.done()