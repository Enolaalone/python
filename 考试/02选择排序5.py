A = [12, 40, 10, 9, 8, -1, 21, -6]
n = 0

for i in range(len(A) - 1):
    for j in range(i + 1, len(A)):
        if A[i] < A[j]:
            A[i], A[j] = A[j], A[i]
        n += 1
print(A)
print(f'排序%d次' % n)
