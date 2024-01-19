import datetime as dt
import turtle as t
def pointer(length,name,width):
    t.reset()#每执行一次，从新设置
    t.pu()
    t.hideturtle()

    t.begin_poly()#记录图形
    t.fd(length)
    t.end_poly()
    t.register_shape(name,t.get_poly())#注册记录的图形

    a=t.Pen()
    a.shape(name)
    a.shapesize(2,1,width)
    return a#画笔a作为对象返回
print()
#---------------------------------------------

def renew():
    global angle
    tm=dt.datetime.today()#返回当下时间
    t.tracer(100)
    t.clear()
    t.pu()           
    t.goto(0,0)
    t.pd()
    t.write(f'{tm:%Y-%m-%d %H:%M:%S}',align='center',font=('Courier',14,'bold'))#Courier计算机字体
    sp.seth(angle)
    angle+=-5
    t.ontimer(renew,1000)#1s执行程序一次

#----------------------------------------------------------------------------------------------------------------------
A=[6,7,8,9,10,11,12,1,2,3,4,5]
def wheel(r):#r半径
    b = t.Pen()
    b.hideturtle()
    b.pu()
    x,y=b.position()
    b.goto(x,y-r)
    b.pd()
    b.width(10)
    #b.seth(180)
    t.tracer(0)
    for i in A:
        b.write(i, align='center', font=('Courier', 30, 'bold'))
        b.dot(10)
        b.up()
        b.circle(r, -30)
        b.pd()
    for i in range(72):
        b.dot(6)
        b.up()
        b.circle(r, -5)
        b.pd()
    t.tracer(1)





window=t.Screen()#设定屏幕

wheel(200)
angle=0#设定初始角
sp=pointer(100,'及你太美',10)
renew()#死循环自己调用自己

window.mainloop()#使屏幕持续存在