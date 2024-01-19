
ls=[[12,0,8,9,6,1,21,46],[3,88,-2,90,100],[6,-3,9,12,44,0,50,70,-23,8]]

def px(ls):
    n=0
    for k in range(len(ls)):
        for j in range(len(ls[k])-1):
            for i in range(len(ls[k])-j-1):
                if ls[k][i]>ls[k][i+1]:
                    ls[k][i],ls[k][i+1]=ls[k][i+1],ls[k][i]
                n+=1
    return n

px(ls)
print(ls)
print(f'冒泡排序的次数为{px(ls)}次')