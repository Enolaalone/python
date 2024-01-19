import turtle as t
import random as r

def cell(color):
    t.color(color)
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
        if self.status==False:#未被揭开状态----------------------调试改为True
            t.hideturtle()
            t.up()
            t.goto(self.x - 20, self.y - 20)
            t.pd()
            cell('grey')
            t.tracer(1)
        else:
            if self.is_mine==True:#是雷
                #------------
                t.pu()
                t.goto(self.x - 20, self.y - 20)
                t.pd()
                cell('lightgrey')
                # -----------------画雷
                t.hideturtle()
                t.pu()
                t.goto(self.x, self.y - 10)
                t.pd()
                t.color('black')
                t.begin_fill()
                t.circle(mine_size/4)
                t.end_fill()
                # -------------
                t.tracer(1)
            else:
                # -------------------------
                t.pu()
                t.goto(self.x - 20, self.y - 20)
                t.pd()
                cell('lightgrey')
                # 写数字
                t.hideturtle()
                t.color('red')
                t.pu()
                t.goto(self.x, self.y-10 )
                t.pd()
                t.write(self.number,align='center',font=('宋体',15,'bold'))

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
#----------------------------
# 初始化雷阵列
mines = [[0 for _ in range(col)] for _ in range(row)]#初始化雷阵

for i in range(row):
    for j in range(col):
        x=(mine_size-width)/2+j*mine_size#x坐标
        y=(-mine_size+width)/2-i*mine_size-(height-width)/2+10#y坐标(height-width)/2+10保证接触底线
        mines[i][j]=Mine(x,y)
#------------------放置地雷-----------------
#print(mines)
n=1
while n<=10:
    a,b=r.randint(0,9),r.randint(0,9)
    if mines[a][b].is_mine==False:
        print(1)
        mines[a][b].is_mine=True
        n+=1

for i in range(row):
    for j in range(col):
        mines[i][j].reveal()





t.done()