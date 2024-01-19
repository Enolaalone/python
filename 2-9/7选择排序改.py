ls=[12,40,10,9,8,-1,21,-6]

n=0
for i in range(len(ls)-1):
    f=i
    for j in range(i+1,len(ls)):
        if ls[j]>ls[f]:
            f=j
    if ls[f]!=ls[i]:
        ls[f],ls[i]=ls[i],ls[f]
        n+=1

print(ls)
print('排序%d次'%n)