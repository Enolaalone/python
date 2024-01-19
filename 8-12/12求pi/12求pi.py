import random
import math

while True:
    n = input('1.公式法      2.pi/4法     3.蒙特卡洛法')
    if n == '1':
        k = 0
        pi = 0
        while k < 100:
            pi+=1 / pow(16, k) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
            k+=1
        print(f'公式法；{pi:.10f}')

    elif n == '2':
        total,t,s,n=0.0,1.0,1,1.0
        while math.fabs(t)>=1e-6:
            total+=t
            s=-s
            n+=2
            t=s/n
        pi=4*total
        print(f'pi/4:{pi:.10f}')

    elif n=='3':
        b=0
        for i in range(1000*1000):
            x=random.random()
            y=random.random()
            distance=math.sqrt(x**2+y**2)
            if distance<=1:
                b+=1
        pi=4*b/(1000*1000)
        print(f'蒙特卡洛:{pi:.10f}')

