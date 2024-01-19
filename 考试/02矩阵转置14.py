ls1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
ls2 = []

for i in range(len(ls1[0])):
    A=[]
    for j in range(len(ls1)):
        A.append(ls1[j][i])
    ls2.append(A)

for i in ls1:
    for j in i:
        print(j,end=' ')
    print()

print()

for i in ls2:
    for j in i:
        print(j,end=' ')
    print()