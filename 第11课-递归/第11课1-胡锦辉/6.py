def jia(n):
    if n==1:
        return 1
    else:
        return (-1)**(n-1)*(2*n-1)+jia(n-1)
print(jia(8))