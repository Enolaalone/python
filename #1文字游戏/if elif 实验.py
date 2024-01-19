a=100

#只会执行elif a<=100
if a<90:
    print(90)
elif a<=100:
    print(100)
elif a<=1000:
    print(1000)
else:
    print(10000)

print('================================================================')
#会执行a<=100 和 a<=1000
if a<90:
    print(90)
if a<=100:
    print(100)
if a<=1000:
    print(1000)
else:
    print(10000)