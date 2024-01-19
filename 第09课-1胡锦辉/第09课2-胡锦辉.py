

a=input('你是第一个报数的人吗?y/n')
if a=='y':
    print('报两 个数字')
    d = 2
    while d<30:
        b=int(input('对手报的数字个数'))
        c=3-b
        print(f'报{c}个数')
        d+=3
else:
     d=int(input('对手第一轮报个数'))
     print(f'报{3-d}个数')
     while d<30:
        b=int(input('对手报的数字个数'))
        c=3-b
        print(f'报{c}个数')
        d+=3


