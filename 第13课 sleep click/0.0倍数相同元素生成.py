import random


A=[ '\u264B','\u2648','\u2649','\u264F', '\u264E', '\u264A', '\u264D', '\u2653', '\u264C','\u2652','\u2650']
print(A)

B=[]#需要生成的集合
b=random.randint(0,len(A)-1)
for i in range(100):
    if (i+1)%9==0:#如果是九的倍数
        B.append(A[b])
    else:
        a=random.randint(0,len(A)-1)
        B.append(A[a])
print(B)
print(B[8],B[17],B[26],B[35])