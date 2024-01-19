a='y'
while a=='y':
    height=float(input('请输入你的身高(米）'))
    weight=float(input('请输入你的体重（千克）'))
    IBM=weight/(height**2)
    if IBM<18:
        print('瘦子')
    elif 18<=IBM<=24:
        print('刚刚好')
    elif 24<=IBM<=28:
        print('微胖')
    else:
        print('胖')
    a=input('是否再玩一次y/n')