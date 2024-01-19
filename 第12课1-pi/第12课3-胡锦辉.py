A=[]
B=[]
C=[]#放结果

for x in range(0,51,10):  # for in试错，x.表示10n个一角
    for y in range(0,51-x,5):#y。表示5n个一角
        z=50-x-y#z。表示n个一角
        if (x*(1/10)+y*(1/10)+z*(1/10)==5):#5元
            A.append(x*(1/10))
            B.append(y*(1/10)/(1/2))  # 装结果
            C.append(z)
n=len(A)
for i in range(len(A)):
    print(i+1,'1元',A[i],'\t5角',B[i],'\t1角',C[i],)  # 显示结果
print('共%d种方案'%n)