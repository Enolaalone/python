n=1000
for j in range(2,n+1):#判断[2弹幕,1000]的数
    for i in range(2,j):#用[2弹幕,j-1报告统计]判断
        if j%i==0:
            break
    else:#如果满足素数条件输出，注意同for对齐
        print(j)

