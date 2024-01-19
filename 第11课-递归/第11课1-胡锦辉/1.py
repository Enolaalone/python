
def age(n):
    if n==5:
        return 10
    else:
        return age(n+1)+2

print(age(1))
