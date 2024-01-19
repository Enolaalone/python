a=int(input('一个数'))
b=a//1000
c=a//100%10
d=a//10%10
e=a%10
sum=b+c+d+e
print(sum)

a = input('一个数')
s = 0
for i in a:
    s += int(i)
    print(s)
print(s)