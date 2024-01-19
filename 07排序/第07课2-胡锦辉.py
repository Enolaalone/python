#冒泡排序
ls=[12,40,10,9,8,-1,21,-6]
n=0
for j in range(len(ls)-1):#除去最后一个数，其他数都要排序
    for i in range(len(ls)-j-1):#比较次数依次减少1
        if ls[i]<ls[i+1]:#小数依次向后浮动
            ls[i],ls[i+1]=ls[i+1],ls[i]
        n+=1

print(ls)
print(f'冒泡排序的次数为{n}次')

