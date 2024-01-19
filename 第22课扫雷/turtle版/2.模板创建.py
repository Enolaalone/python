import turtle as t

def cell():
    t.color('grey')
    t.begin_fill()
    for i in range(4):
        t.fd(40)
        t.left(90)
    t.end_fill()
    t.color('white')
    for i in range(4):
        t.fd(40)
        t.left(90)
    t.end_fill()



class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.number=0#周围雷数
        self.status=False#是否揭开
        self.is_mine=False#是否是雷

    def reveal(self):#雷的各种运动
        t.tracer(0)
        if self.status==False:#未被揭开状态
            t.hideturtle()
            t.up()
            t.goto(self.x - 20, self.y - 20)
            t.pd()
            cell()
            t.tracer(1)
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
                cell()
                t.tracer(1)
            else:
                # 写数字
                t.hideturtle()
                t.color('red')
                t.pu()
                t.goto(self.x- 20, self.y )
                t.pd()
                t.write(self.number,align='center',font=('宋体',14,'normal'))
                # -------------------------
                t.pu()
                t.goto(self.x - 20, self.y - 20)
                t.pd()
                cell()
                t.tracer(1)
'''mine=Mine(0,0)#创建具体的对象才可继续调用内部函数
mine.reveal()'''



width=400
height=500
row=10
col=10
mine_size = 40  #雷大小
#----------游戏初始化-----------------
game=t.Screen()#导入屏幕
game.title('扫雷')#取名
game.bgcolor('white')#设置背景颜色
game.setup(width+10,height)#游戏窗口大小
#----------------------------------------
# 初始化雷阵列
mines = [[0 for _ in range(col)] for _ in range(row)]#初始化雷阵

for i in range(row):
    for j in range(col):
        x=(mine_size-width)/2+j*mine_size#x坐标
        y=(-mine_size+width)/2-i*mine_size-(height-width)/2+10#y坐标(height-width)/2+10保证接触底线
        mines[i][j]=Mine(x,y)
        mines[i][j].reveal()









t.done()