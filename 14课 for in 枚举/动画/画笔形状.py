import turtle
#注册画笔
a=turtle.Pen()
b=turtle.Pen()
c=turtle.Pen()
d=turtle.Pen()

turtle.register_shape('lang.gif')#注册turtle
turtle.register_shape('yang.gif')
turtle.register_shape('cai.gif')
turtle.register_shape('chuan.gif')
#需要将相应gif图片放到对应项目下
turtle.up()
'''
a.shape('lang.gif')
b.shape('cai.gif')
c.shape('lang.gif')
d.shape('lang.gif')
'''
def bi(name,size,shape):#画笔生成
    name=turtle.Pen()
    name.pensize(size)
    name.shape(shape)


bi('x',1,'chuan.gif')



turtle.done()