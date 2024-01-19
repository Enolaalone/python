import random as r

class Mine:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.txt='\u25A0'
        self.number=0


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
#-----------------------写数字
print()
for i in range(10):
    for j in range(10):
        if mines[i][j].txt!='*':
            num=0
            for k in range(i-1,i+2):
                for l in range(j-1,j+2):
                    if (0<=k<=9) and (0<=l<=9):#防止越界
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

