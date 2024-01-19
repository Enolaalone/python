import turtle,time
def p(x,y):#onscreenclick内置函数，（x,y)必须有测定坐标值
    global k
    k=1#global使k全局化,函数内k与函数外k等价

k=0
turtle.onscreenclick(p)#检测鼠标点击
for i in range(20):
    turtle.goto(5*i,0)
    turtle.circle(i+10)
    time.sleep(0.06*i)#-------------时间暂缓
    if k==1:#-----------点击后结束程序
        break
#---------------------------------time.sleep函数运行越来越慢
