import random
A=['0','1报告统计','2弹幕','3小学算术','4.进度条','5','6','7','8','9']

account1={'100': '01', '101': '02'}
mima1={'100': '123456', '101': '123456'}
while (1):
    verify = ''
    for i in range(4):  # 四位验证码
        a = random.randint(0, 9)
        verify += A[a]  # 生成验证码
    account=input('请输入账号')
    mima=input('请输入密码')
    print('验证码:'+verify)
    test = input('输入验证码' )
    #print(mima1.get(account))
    if (account in account1) and (mima in mima1.get(account)) and (test==verify):#后者检查密码
        print(f'{account1[account]}欢迎登录')
        break
    else:
        print('账号,密码或验证码有错误,再次输入')
        continue