def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
num=int(input('一个数'))
if prime(num):
    print(num,'是素数')
else:
    print(num,'不是素数')