def age(n):
    if n==5:
        return 10
    else:
        return age(n+1)+2

print(age(1))

def tao(n):
    if n==10:
        return 1
    else:
        return (tao(n+1)+1)*2
print(tao(1))

def jie(n):
    if n==1:
        return 1
    else:
       return jie(n-1)*n
print(jie(5))

def fei(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fei(n-1)+fei(n-2)

print(fei(15))
def jia(n):
    if n==1:
        return 1
    else:
        return 1/(2*n-1)+jia(n-1)

print('{:.4f}'.format(jia(6)))

def jia(n):
    if n==1:
        return 1
    else:
        return (-1)**(n-1)*(2*n-1)+jia(n-1)
print(jia(8))

def jia(n):
    if n==1:
        return 1
    else:
        return (-1)**(n-1)*1/(2*n-1)+jia(n-1)
print('{:.4}'.format(jia(7)))