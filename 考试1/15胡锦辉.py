ls=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
for i in range(len(ls)):
    print()
    for j in ls[i]:
        print(f'{j}',end='\t')
l1=[]
for j in range(len(ls[0])):
    A = []
    for i in range(len(ls)):
        A.append(ls[i][j])
    #print(A)
    l1.append(A)

print()
#print(l1)

for i in range(len(l1)):
    print()
    for j in l1[i]:
        print(f'{j}',end='\t')

