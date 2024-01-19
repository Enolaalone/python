class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='\u25A1'
    def __str__(self):#单纯返回值
        return ('mine%d%d'%(self.x,self.y))

mines=[[0 for _ in range(10)] for _ in range(10)]
print(mines)


for i in range(10):#将雷装入列表
    for j in range(10):
        mines[i][j]=Mine(i,j)
#----------------------------------
#显示雷
mines[0][0]='*'
mines[0][1] = ' 3'
for i in range(10):
    for j in range(10):
        print(mines[i][j],end='')
    print()


print('',end='\t')
for k in range(10):
    print(k,end='\t')
print()
for i in range(10):
    print(i,end='\t')
    for j in range(10):
        print(mines[i][j],end='\t')
    print()