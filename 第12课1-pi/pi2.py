import math
total,s,n,t=0.0,1,1.0,1.0#变量赋予初始值
while (math.fabs(t)>=1e-6):#算到很小的项
    total+=t#累加
    n+=2#分子单数增加
    s=-s#控制正负变化
    t=s/n#构造分数
pi=4*total
print('{:.10f}'.format(pi))#保留10小数

math.fabs()#绝对值函数
1e-6#10的-16次方