A=[]
B=[]
C=[]#放结果
for x in range(0,101,5):  # for in试错，x公鸡
    for y in range(0,101-x,3):#y母鸡
        z=100-x-y#z小鸡
        if (x//5+y//3+z//(1/3) == 100)and(x+y+z==100):#百元百只
            A.append(x//5)#//即先做除法（/），然后向下取整（floor），至少有一方是float型时，结果为float型；两个数都是int型时，结果为int型
            B.append(y//3)  # 装结果
            C.append(z*3)
print('公鸡',A,'\n母鸡',B,'\n小鸡',C)  # 显示结果