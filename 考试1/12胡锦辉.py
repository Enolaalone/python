def shusu():
    a=int(input('一个数'))
    if a<2:
        print(f"{a}不是")
    else:
        for i in range(2,a):
            if a%i==0:
                print(f"{a}不是")
        else:
            print(f"{a}是素数")
print(shusu())