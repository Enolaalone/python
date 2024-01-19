def prime(s):
        for i in range(2,s):
            if s%i==0:#判断是否为素数
                return False
        else:#注意else的位置
            return True

A=[]#建立集合A用于存储素数对
c=0
for i in range(1000,2001):
    if prime(i) and prime(i+2):#须同时满足i和i+2都是素数
        A.append([i,i+2])
        c+=1#利用循环次数记录孪生素数对

print(A)
print('1000-2000之间共有%d对孪生素数对'%c)








