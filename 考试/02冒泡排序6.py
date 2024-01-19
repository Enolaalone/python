A = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0

for i in range(len(A) - 1):
    for j in range(len(A) - 1 - i):
        if A[j] < A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
        n += 1

print(A)
print("冒泡排序%d次" % n)
