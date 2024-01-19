import datetime as dt
import turtle as t
A=[6,7,8,9,10,11,12,1,2,3,4,5]#画表盘
a=t.Pen()#秒
b=t.Pen()#分钟
c=t.Pen()#小时
def pointer(length,name,width,a,color):#画指针
    t.reset()#每执行一次，从新设置
    t.hideturtle()
    t.pu()
    t.begin_poly()#记录图形
    t.fd(length)#从0开始
    t.end_poly()
    t.register_shape(name,t.get_poly())#注册记录的图形
    #a.hideturtle()
    a.pencolor(color)
    a.shape(name)
    a.shapesize(2,1,width)

    return a#画笔a作为对象返回

#---------------------------------------------

def renew():
    global m
    global h
    t.tracer(0)
    t.clear()
    tm = dt.datetime.today()  # 返回当下时间
    #print(tm)
    s = tm.second#秒
    m = tm.minute#分
    #print(m)
    h = tm.hour#小时
    t.pu()
    t.goto(-6,0)
    t.pd()
    t.write(f'{tm:%Y-%m-%d %H:%M:%S}', align='center', font=('Courier', 14, 'bold'))  # Courier计算机字体
    sec.seth(180 - 6*s)#秒钟，起始为12
    minute.seth(180-6*m)#分钟，起始为12
    hour.seth(180-30*h)
    t.tracer(1)
    t.ontimer(renew,1000)#1s执行程序一次
#----------------------------------------------------------------------------------------------------------------------
#============================画表盘
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

    for i in A:#数字部分
        b.write(i, align='center', font=('Courier', 30, 'bold'))
        b.dot(10)
        b.up()
        b.circle(r, -30)
        b.pd()

    for i in range(60):#小格子
        b.dot(6)
        b.up()
        b.circle(r, -6)
        b.pd()
    t.tracer(1)
    t.seth(0)

window=t.Screen()#设定屏幕
wheel(200)
sec=pointer(90,'秒针',10,a,'black')
minute=pointer(70,'分针',10,b,'blue')
hour=pointer(40,'时针',10,c,'red')
renew()#死循环自己调用自己
window.mainloop()#使屏幕持续存在