def Sum(n):
    if n==1:
        return 1
    else:
        return Sum(n-1)+n

print(Sum(100))