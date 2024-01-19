def tao(n):
    if n==10:
        return 1
    else:
        return (tao(n+1)+1)*2
print(tao(1))