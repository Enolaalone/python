c='y'
while c=='y':
    a=int(input('起始年'))
    b=int(input('终止年'))
    A=[]
    for i in range(a,b+1):
        if (i%4==0 and i%100!=0) or(i%400==0):
            A.append(i)
        else:
            continue
    print(f'闰年个数为{len(A)}')
    print(A)
    c=input('是否再玩一次y/n')