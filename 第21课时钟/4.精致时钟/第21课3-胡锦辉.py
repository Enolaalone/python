import turtle as t
import datetime as dt

t.register_shape('C.gif')
a=t.Pen()
b=t.Pen()
c=t.Pen()
d=t.Pen()
d.shape('C.gif')

def pointer(length,name,width,a,color):#画指针
    t.reset()#每执行一次，从新设置
    t.hideturtle()
    t.pu()
    t.begin_poly()#记录图形

    t.fd(length)#从0开始
    t.right(90)

    t.end_poly()
    t.register_shape(name,t.get_poly())#注册记录的图形
    #a.hideturtle()
    a.pencolor(color)
    a.shape(name)
    a.shapesize(1,1,width)

    return a#画笔a作为对象返回
def renew():
    global s
    global m
    global h
    t.tracer(0)
    t.clear()
    tm = dt.datetime.today()  # 返回当下时间
    #print(tm)
    #--------------------联动效果

    if s==60:#满一分钟
        s=0
        m+=1
    if m==60:#满一小时
        m=0
        h+=1
    if h==24:
        h=0
    t.pu()
    t.goto(-5, 100)
    t.pd()
    t.write(f'北京时间', align='center', font=('宋体', 50, 'normal'))  # Courier计算机字体
    t.pu()
    t.goto(-20,0)
    t.pd()
    t.write(f'{tm:%Y-%m-%d %H:%M:%S}', align='center', font=('Courier', 30, 'bold'))  # Courier计算机字体
    sec.seth(180 - 6*s)#秒钟，起始为12
    minute.seth(180-6*m-6*(s/60))#分钟，起始为12
    hour.seth(180-30*h-30*(m/60))
    t.tracer(1)
    s += 1#加一秒
    t.ontimer(renew,1000)#1s执行程序一次


window=t.Screen()#设定屏幕
sec=pointer(250,'秒针',12,a,'purple')
minute=pointer(200,'分针',12,b,'skyblue')
hour=pointer(150,'时针',12,c,'pink')
tm = dt.datetime.today()
s = tm.second  # 秒
m = tm.minute  # 分
h = tm.hour  # 小时
renew()#死循环自己调用自己
window.mainloop()#使屏幕持续存在