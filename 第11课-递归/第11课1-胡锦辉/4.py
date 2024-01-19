def fei(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fei(n-1)+fei(n-2)

print(fei(15))