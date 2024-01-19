import random
A=['0','1报告统计','2弹幕','3小学算术','4.进度条','5','6','7','8','9']
verify=''
for i in range(4):#四位验证码
    a=random.randint(0,9)
    verify+=A[a]#生成验证码
print('验证码：'+verify)
test=input('输入验证码')
if test==verify:
    print('123')