ls=[12,40,10,9,8,-1,21,-6]

#第一个数和剩下数比较
for i in range(len(ls)-1):
    if ls[0]>ls[i+1]:
        ls[0],ls[i+1]=ls[i+1],ls[0]
print(ls)#最小的数会在最前面，大数会交换到后面

for i in range(len(ls)-2):#第二个数只需要和，除去它自己和第一个数以外的数比较
    if ls[1]>ls[i+2]:
        ls[1],ls[i+2]=ls[i+2],ls[1]
print(ls)#第二小的数在第二