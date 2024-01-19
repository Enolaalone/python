A=[]
B=[]
C=[]#放结果

for x in range(0,51,3):  # for in试错，x.表示男人饭钱
    for y in range(0,51-x,2):#y。表示女人饭钱
        z=50-x-y#z。孩子饭钱
        if (x//3+y//2+z==30):#30人
            A.append(x//3)
            B.append(y//2)  # 装结果
            C.append(z)
n=len(A)
for i in range(len(A)):
    print('男人',A[i],'\t女人',B[i],'\t小孩',C[i])  # 显示结果
print('\n共%d种方案'%n)