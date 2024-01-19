import random as r

class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='\u25A0'
    def __str__(self):#单纯返回值
        return ('mine%d%d'%(self.x,self.y))

mines=[[0 for _ in range(10)] for _ in range(10)]
print(mines)


for i in range(10):
    for j in range(10):
        mines[i][j]=Mine(i,j)

n=1
while n<=10:
    a,b=r.randint(0,9),r.randint(0,9)
    if mines[a][b].txt!='*':
        mines[a][b].txt ='*'
        n+=1

print('', end='\t')
for i in range(10):
    print(i, end='\t')
print()
for i in range(10):
    print(i, end='\t')
    for j in range(10):
        print(mines[i][j].txt, end='\t')
    print()
