def jie(n):
    if n==1:
        return 1
    else:
       return jie(n-1)*n
print(jie(5))