class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='\u25A0'
    def __str__(self):
        return ('mine%d%d'%(self.x,self.y))
#-------------雷盘---------------------------------------------------
mines=[[0 for _ in range(10)] for _ in range(10)]
#print(mines)
#---------------------------------将雷装入列表--------------------------------
for i in range(10):
    for j in range(10):
        mines[i][j]=Mine(i,j)

#---------------str类状态--------------------------
for i in range(10):
    for j in range(10):
        print(mines[i][j],end='')
    print()

for i in range(10):
    for j in range(10):
        print(mines[i][j].txt,end='\t')
    print()