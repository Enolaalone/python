k='y'
while k=='y':
    begin_year=int(input('起始年'))
    end_year=int(input('结束年'))
    A=[]
    for i in range(begin_year,end_year+1):
        if i%400==0:
            A.append(i)
        elif i%100!=0 and i%4==0:
            A.append(i)

    for i in range(len(A)):
        print(f'{A[i]},',end=' ')
        if (i+1)%10==0:
            print()
    print()
    k=input('是否再玩一次？y/n')
