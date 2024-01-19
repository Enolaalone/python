for i in range(1,1000):
    if (i%3==0) or ('3'in str(i)):
        print('过,',end='')
    else:
        print(f'{i},',end='')

    if (i+1)%10==0:
        print()