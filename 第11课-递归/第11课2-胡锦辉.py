a=int(input('输入求和的项数'))
def fei(n):#求第n个数
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fei(n-1)+fei(n-2)#前n-2项 加 n-1项

def fei_he(n):
    if n==1:
        return 1
    else:
        return fei_he(n-1)+fei(n)#第n-1的和 加上第n项
print(fei_he(a))