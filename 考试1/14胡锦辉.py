ls1=[12,40,10,9,8,-1,21,-6]
ls2=[12,7,10,9,88,-1,21,-6,10]
A=[]
B=[]
C=[]
for i in ls2:
    if i not in ls1:
        A.append(i)
for i in ls1:
    if i not in ls2:
        B.append(i)
    else:
        C.append(i)
print(f'ls2有ls1无{A},ls1有ls2无{B},相同{C}')