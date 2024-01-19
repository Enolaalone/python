for j in range(9, 0, -1):  # 从9到1逆向循环
    for i in range(1, j + 1):
        print('%dx%d=%d' % (i, j, j * i), end='\t')
    print()

for j in range(1, 10):
    for i in range(1, j + 1):
        print('%dx%d=%d' % (i, j, j * i), end='\t')
    print()
