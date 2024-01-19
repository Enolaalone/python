a='y'
while a=='y':
    A=[]#装结果的集合
    a=int(input('输入几位水仙花'))
    for i in range(10**(a-1),10**a):#枚举数字
        s = 0
        for j in range(a):#判断水仙花条件
            s+=(i//(10**j)%10)**a
        if s == i:#判断水仙花条件
            A.append(i)
    print(A)#------------8位时间久
    a=input('是否再玩一次？y/n')
