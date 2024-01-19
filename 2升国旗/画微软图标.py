#from turtle import color
import time


#--------定义画色块模块--------
def square(x,color):
    import turtle as t  #用t简化turtle
    t.color( color) #调用颜色模块
    t.begin_fill()

    t.left(x)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(200)
    t.left(90-x)

    t.end_fill()




#------作图-------
square(0,'yellowgreen')
square(90,'orangered')
square(180,'dodgerblue')
square(-90,'orange')


#---------延迟结束-------
input("Press Enter to exit...")

#time.sleep(5)
#turtle.done()  # 可以使画图窗口持续存在


