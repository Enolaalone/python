
#改进选择排序
ls=[12,40,10,9,8,-1,21,-6]
n=0

for j in range(len(ls)-1):
    f=j#位置信息
    for i in range(len(ls)-1-j):
        if ls[f]<ls[j+i+1]:
            f=j+i+1#交换位置信息，不该变顺序，确认该数列表位置
    ls[f], ls[j] = ls[j],ls[f]#改变位置
    n+=1
print(ls)
print(f'改进选择排序的次数为{n}次')



#选择排序
ls=[12,40,10,9,8,-1,21,-6]
n=0
for j in range(len(ls)-1):#除最后一个数外其他数都要排序
    for i in range(len(ls)-1-j):#每个数的比较次数
        if ls[j]<ls[j+i+1]:
            ls[j],ls[j+i+1]=ls[j+i+1],ls[j]#交换位置
        n+=1

print(ls)
print(f'选择排序的次数为{n}次')






ls=[12,40,10,9,8,-1,21,-6]
n=0

for j in range(len(ls)-1):
    f=j
    for i in range(len(ls)-1-j):
        if ls[f]<ls[j+i+1]:
            f=j+i+1
    if f!=j:#如果位置信息与原来不同再改变
        ls[f], ls[j] = ls[j],ls[f]
        n+=1
print(ls)
print(f'最优选择排序的次数为{n}次')




