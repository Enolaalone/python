#--------模块定义---------
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

#------作图-----------
square(0,'yellowgreen')
square(90,'orangered')
square(180,'dodgerblue')
square(-90,'orange')


#---------延迟结束-------
t.done()