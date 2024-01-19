def prime(s):
    for i in range(2, s):
        if s % i == 0:
            return False
    else:
        return True


A = []
n = 0
for i in range(1000, 2001):
    if prime(i) and prime(i + 2):
        A.append([i, i + 2])
        n += 1

print(A)
print("1000-2000之间共有%d对素数对" % n)
