import random as r

class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='\u25A0'
        self.number=0
        self.statue=False#雷的状态
    #def click(self):
#----------------------------------------
#------------------扩展
def expand(x, y):#
    if x < 0 or x >= 10 or y < 0 or y >= 10 or mines[x][y].statue or mines[x][y].txt=='*':
        return  # 超出边界或者方块已被访问，停止扩展
    mines[x][y].statue = True  # 将此方块标记为已访问
    #print(f'{x,y}True')

    if mines[x][y].number > 0:
        return  # 如果方块周围有雷，停止扩展
    # 递归检查周围的8个方块
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                expand(x + dx, y + dy)



mines=[[0 for _ in range(10)] for _ in range(10)]
#-----------------生成雷-----------------------
for i in range(10):
    for j in range(10):
        mines[i][j]=Mine(i,j)
n=1
while n<=10:#生成10个雷
    a,b=r.randint(0,9),r.randint(0,9)
    if mines[a][b].txt!='*':
        mines[a][b].txt ='*'
        n+=1


#-----------------------明示雷-----------
print('', end='\t')
for i in range(10):
    print(i, end='\t')
print()
for i in range(10):
    print(i, end='\t')
    for j in range(10):
        print(mines[i][j].txt, end='\t')
    print()

print('#---------------------------------------------------')
print()#--------------------------显示雷数---------------
for i in range(10):
    for j in range(10):
        if mines[i][j].txt!='*':
            num=0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if  (0<=k<=9) and (0<=l<=9):#防止越界
                        if mines[k][l].txt=='*':
                            num+=1
            mines[i][j].number=num


print('', end='\t')
for i in range(10):
    print(i, end='\t')
print()
for i in range(10):
    print(i, end='\t')
    for j in range(10):
        print(mines[i][j].number, end='\t')
    print()

#----------------------------------------------------------
#游戏初始化
# -----列号------------------
print('', end='\t')
for i in range(10):
    print(i, end='\t')
print()
for i in range(10):
    print(i, end='\t')#行号
    for j in range(10):
        if not mines[i][j].statue:
            print('\u25A0', end='\t')
        else:
            print(mines[i][j].number, end='\t')
    print()

Game=0
while Game==0:
    a=input('输入雷号:行，列 x,y')
    a1,a2=a.split(',')
    expand(int(a1), int(a2))
    #mines[int(a1)][int(a2)].statue=True#揭开状态改变

    #-------------------------------------

    if mines[int(a1)][int(a2)].txt == '*':#踩雷----打印所有雷
        for i in range(10):
            for j in range(10):
                if mines[i][j].txt=='*':
                    mines[i][j].statue=True#将所有雷翻开
        #-----列号------------------
        print('', end='\t')
        for i in range(10):
            print(i, end='\t')
        print()
        for i in range(10):
            print(i, end='\t')  # 行号
            for j in range(10):
                # if mines[i][j].number==0:
                # mines[i][j].statue=True
                if not mines[i][j].statue:
                    print('\u25A0', end='\t')
                else:
                    if mines[i][j].txt == '*':
                        print(mines[i][j].txt, end='\t')
                    else:
                        if mines[i][j].number == 0:  # 如果是0打印空
                            print('\u25A1', end='\t')
                        else:
                            print(mines[i][j].number, end='\t')
            print()
            Game=1
    else:#----未踩雷

        # -----列号------------------
        print('', end='\t')
        for i in range(10):
            print(i, end='\t')
        print()
        for i in range(10):
            print(i, end='\t')#行号
            for j in range(10):
                #if mines[i][j].number==0:
                    #mines[i][j].statue=True
                if not mines[i][j].statue:
                    print('\u25A0', end='\t')
                else:
                    if mines[i][j].txt == '*':
                        print(mines[i][j].txt, end='\t')
                    else:
                        if mines[i][j].number == 0:  # 如果是0打印空
                            print('\u25A1', end='\t')
                        else:
                            print(mines[i][j].number, end='\t')
            print()

print('Game over!')



