import random
A={}
def jia():
    a =random.randint(0, 99)
    b =random.randint(0, 100-a)
    a1=str(a)
    b1=str(b)
    a1 += '+'
    a1 += b1
    a1 += '='
    A[a+b] = a1

def jian():
    a = random.randint(0, 99)

    b = random.randint(0, a)
    a1=str(a)
    b1=str(b)
    a1 += '-'
    a1 += b1
    a1 += '='
    A[a - b] = a1

def cheng():
    while True:
        a = random.randint(0, 99)
        b = random.randint(0, 10)
        if a*b<100:
            break
    a1=str(a)
    b1=str(b)
    a1+='X'
    a1 += b1
    a1 += '='
    A[a * b] = a1

def chu():
    while True:
        a = random.randint(0, 99)
        b = random.randint(1, a)
        if a%b==0:
            break
    a1=str(a)
    b1=str(b)
    a1 += '/'
    a1 += b1
    a1 += '='
    A[int(a/b)] = a1
for i in range(2):
    jia()
    jian()
    cheng()
    chu()
for j in range(2):
    k=random.randint(1,4)
    if k==1:
        jian()
    if k==2:
        jian()
    if k==3:
        cheng()
    if k==4:
        chu()
print(A)

for key,value in A.items():
    print(value)

B=[]
for i in range(10):
    a=int(input('输入结果'))
    B.append(a)

grade=0
n=0
for key,value in A.items():
    if B[n]==key:
        grade+=10
    n+=1

print(grade)

