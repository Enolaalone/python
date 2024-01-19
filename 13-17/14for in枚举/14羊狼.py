import Data1
import random as r

while True:
    a = r.randint(0, len(Data1.A[0]) - 1)
    k = Data1.A[0].pop(a)
    if Data1.subject[Data1.A[0][0]] + Data1.subject[Data1.A[0][-1]] == 0:
        Data1.A[0].append(k)
    else:
        Data1.A[2].append(k)
        print(Data1.A)
        break

s = 1
a = r.randint(0, len(Data1.A[0]) - 1)
Data1.A[2].append(Data1.A[0].pop(a))
print(Data1.A)

while True:
    if s == 1:
        n1 = 2
        n2 = 0
    else:
        n1 = 0
        n2 = 0
    Data1.A[n2].append(Data1.A[n1].pop(0))
    print(Data1.A)
    if Data1.subject[Data1.A[2][0]] + Data1.subject[Data1.A[2][-1]] != 0 and s == -1:
        Data1.A[2].append(Data1.A[0][0])
        print(Data1.A)
        break
    s = -s
