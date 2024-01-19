import random as r
A=[]
n=0
for _ in range(10):
    a=r.randint(1,100)
    A.append(a)

# print(A)

for i in range(len(A)-1):
    for j in range(len(A)-1-i):
        if A[j]<A[j+1]:
            A[j],A[j+1]=A[j+1],A[j]
        n+=1
print(n)
print(A)