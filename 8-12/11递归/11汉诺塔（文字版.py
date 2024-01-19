def hanoi_tower_list(n, a, b, c):
    if n == 1:
        c.append(a.pop())
        print(A, B, C)

    else:
        hanoi_tower_list(n - 1, a, c, b)
        c.append(a.pop())
        print(A, B, C)
        hanoi_tower_list(n - 1, b, a, c)


def hanoi(n):
    for i in range(n, 0, -1):
        A.append(i)
    hanoi_tower_list(n, A, B, C)


A = []
B = []
C = []
hanoi(3)
