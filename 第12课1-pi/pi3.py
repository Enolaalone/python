import random
import math

b=0
for i in range(1000*1000):
    x=random.random()#随机生成0-1之间的数
    y=random.random()
    disrance=math.sqrt(x**2+y**2)
    if disrance<=1:
        b+=1
pi=(b/(1000*1000))*4
print('{:.10f}'.format(pi))
import random

random.Random()#随机生成0-1间的小数