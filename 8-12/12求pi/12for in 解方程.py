A=[];B=[];C=[]
for x in range(0,101,5):
    for y in range(0,101-x,3):
        z=100-x-y
        if (x//5)+(y//3)+(3*z)==100:
            A.append(x//5)
            B.append(y//3)
            C.append(3*z)
for i in range(len(A)):
    print(f'公鸡：{A[i]};母鸡：{B[i]};小鸡：{C[i]}')
print(len(A),'种方案')
print()
A = [];B = [];C = []
for x in range(0, 51, 10):
    for y in range(0, 51 - x, 5):
        z = 50 - x - y
        A.append(x // 10)
        B.append(y // 5)
        C.append(z)
for i in range(len(A)):
    print(f'一元：{A[i]};五角：{B[i]};一角：{C[i]}')
print(len(A),'种方案')
print()
A = [];B = [];C = []
for x in range(0, 51, 3):
    for y in range(0, 51 - x, 2):
        z = 50 - x - y
        if (x//3)+(y//2)+z==30:
            A.append(x // 3)
            B.append(y // 2)
            C.append(z)
for i in range(len(A)):
    print(f'男人：{A[i]};女人：{B[i]};小孩：{C[i]}')
print(len(A),'种方案')
print()