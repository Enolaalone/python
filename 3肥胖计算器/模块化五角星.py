import turtle as t
def star():
    import math
    t.speed(1)
    t.seth(math.degrees(math.tan(7/2)))#设定起始角
    li=[]#---定义集合
    # 画圆形，标记位置
    for i in range(5):
        t.circle(-40,144)#------标记五个角位置------
        t.pencolor("white")

        # turtle.dot()
        li.append(t.pos())#-----将标记位置放入集合

    t.pencolor('yellow') #修改笔颜色
    t.fillcolor("yellow")
    t.begin_fill()
    t.down()
    t.goto(li[4])#------画笔去到剩下四个点------
    for i in range(5):
        t.goto(li[i])
    t.end_fill()

star()
t.done()





'''append
list_name.append(element)
list_name 是指定的列表。
element 是要添加到列表末尾的元素。
append 是Python中列表（list）对象的一个方法，它用于在列表的末尾添加一个元素。
'''