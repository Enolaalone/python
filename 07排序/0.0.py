ls=[12,40,10,9,8,-1,21,-6]

#第一个数和剩下数比较
for i in range(len(ls)-1):
    if ls[0]>ls[i+1]:
        ls[0],ls[i+1]=ls[i+1],ls[0]
print(ls)#最小的数会在最前面，大数会交换到后面

