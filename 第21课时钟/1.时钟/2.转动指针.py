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
angle=0#设定初始角
sp=pointer(100,'及你太美',10)
renew()#死循环自己调用自己
t.done()