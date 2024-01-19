import datetime as dt
import turtle as t
def pointer(length,name):
    t.reset()#每执行一次，从新设置
    t.pu()
    #t.hideturtle()

    t.begin_poly()#记录图形
    t.fd(length)
    t.end_poly()
    t.register_shape(name,t.get_poly())#注册记录的图形

    a=t.Pen()
    a.shape(name)
    a.shapesize(2,1,10)
    return a#画笔a作为对象返回
print(pointer(100,'及你太美'))

t.done()