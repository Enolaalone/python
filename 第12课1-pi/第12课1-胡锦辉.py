import random
import math
while True:
    n=input('1公式法\t2pi/4公式法\t3蒙特卡洛法\t4结束')
    if n=='1':
        a=0
        pi=0
        while a<=100:
            pi+=1/pow(16,a)*(4/(8*a+1)-2/(8*a+4)-1/(8*a+5)-1/(8*a+6))
            a+=1
        print('公式法{:.10f}'.format(pi))
 

    elif n=='2':
        total,s,n,t=0.0,1,1.0,1.0#变量赋予初始值
        while (math.fabs(t)>=1e-6):#算到很小的项
            total+=t#累加
            n+=2#分子单数增加
            s=-s#控制正负变化
            t=s/n#构造分数
        pi=4*total
        print('pi/4公式法{:.10f}'.format(pi))#保留10小数

    elif n=='3':
        b=0
        for i in range(1000*1000):
            x=random.random()
            y=random.random()
            disrance=math.sqrt(x**2+y**2)
            if disrance<=1:
                b+=1
        pi=(b/(1000*1000))*4
        print('蒙特卡洛法{:.10f}'.format(pi))
    else:
        break