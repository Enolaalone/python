#3位水仙花数

for i in range(1,10):#1报告统计-9最高位
    for j in range(10):#十位
        for k in range(10):#个位
            num=i*100+j*10+k
            if (num==i**3+j**3+k**3):#判断条件是否成立
                print(num)



