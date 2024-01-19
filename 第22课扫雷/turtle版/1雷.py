import turtle as t

class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.number=0#周围雷数
        self.status=False#是否揭开
        self.is_mine=False#是否是雷

    def reveal(self):#雷的各种运动
        if self.status==False:#未被揭开状态
            t.hideturtle()
            t.up()
            t.goto(self.x - 20, self.y - 20)
            t.pd()
            t.color('grey')
            t.begin_fill()
            for i in range(4):
                t.fd(40)
                t.left(90)
            t.end_fill()
        else:
            if self.is_mine==True:#是雷
                #画雷
                t.hideturtle()
                t.pu()
                t.goto(self.x, self.y - 20)
                t.pd()
                t.circle(20)
                #-------------------------
                t.pu()
                t.goto(self.x - 20, self.y - 20)
                t.pd()
                t.color('grey')
                t.begin_fill()
                for i in range(4):
                    t.fd(40)
                    t.left(90)
                t.end_fill()
            else:
                # 写数字
                t.hideturtle()
                t.pu()
                t.goto(self.x- 20, self.y )
                t.pd()
                t.write(self.number,align='center',font=('宋体',14,'normal'))
                # -------------------------
                t.pu()
                t.goto(self.x - 20, self.y - 20)
                t.pd()
                t.color('grey')
                t.begin_fill()
                for i in range(4):
                    t.fd(40)
                    t.left(90)
                t.end_fill()

mine=Mine(0,0)#创建具体的对象才可继续调用内部函数
mine.reveal()
t.done()