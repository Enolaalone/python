ls=[12,40,10,9,8,-1,21,-6]

#-------------------------------------抽象出一般规律
f=0
for i in range(len(ls)-(f+1)):
    if ls[f]>ls[i+1]:
        f=i+1#只交换头衔
ls[0],ls[f]=ls[f],ls[0]#for in结束后在交换内容
print(ls)


#-----------------------------------------
for i in range(len(ls)-1):#进行-1次大的循环比较
    f=i#每次比较开始时f等于要比较的数的头衔
    for j in range(len(ls)-1-i):
        if ls[f]>ls[i+j+1]:
            f=i+j+1#将最小的头衔交换到最前面
    if f!=i:#如果不相等再交换
        ls[i],ls[f]=ls[f],ls[i]
print(ls)
