ls=[12,40,10,9,8,-1,21,-6]

for i in range(len(ls)-1):
    print(ls)

    for j in range(len(ls)-1-i):#每比一轮减1，用i 表现
        if ls[i]>ls[j+i+1]:
            ls[i],ls[j+i+1]=ls[j+i+1],ls[i]
            print(ls)
    print()

print('这是改进')
ls = [12, 40, 10, 9, 8, -1, 21, -6]
for i in range(len(ls)-1):
    print('i',ls)
    f=i
    for j in range(len(ls) - 1 - i):
        if ls[f]>ls[i+j+1]:
            f=i+j+1
    print(f)
    if f!=i:
        ls[f],ls[i]=ls[i],ls[f]
    print(ls)
    print()


