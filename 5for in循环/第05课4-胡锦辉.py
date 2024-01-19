def num(j):#判断是否为素数
    if j<2:
        return False
    for i in range(2, j):
        if j % i == 0:
            return False
    else:
        return True

lit=[]#建立集合
count=0
for j in range(1000, 2000):
    if num(j):#如果满足素数条件就进入集合
        lit.append(j)
        count+=1
print(lit)
print('\n1报告统计-1000之间素数有%d个'%count)



