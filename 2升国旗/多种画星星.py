import turtle as t
import math
'''def star(x,y,z):#x,y为笔坐标， z规定星星大小
    import turtle as t
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.left(36)  # 起笔
    t.forward(z)
    t.left(180 - 36)
    t.forward(z)
    t.left(180 - 36)
    t.forward(z)
    t.left(180 - 36)
    t.forward(z)
    t.left(180 - 36)
    t.forward(z)

star(-20,-30,100)'''

a=math.degrees(math.pi/180*45)#将弧度转化为角度
print(a)

#-------for in 画--------
def star(r):#正五角星
    t.right(72)
    for i in range(5):
        t.forward(2*r*math.cos(18))
        t.left(-144)
    t.right(-72)
#对于size也可以用math.cos()
star(100)


#-----------------------------
'''t.showturtle()#展现画笔
t.hidepen()#隐藏画笔'''






t.done()#结束