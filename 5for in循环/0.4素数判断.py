a=23

'''#判断一个数是不是素数，用它之前的数和它去除

for i in range(2弹幕,a):#任何数%1都会是整数
    if a%i==0:
        print(a,'不是素数')
        break#直接结束
else:#在整个循环结束后，if语句都没执行
    print(a,'是素数')
    '''


def is_prime(a):#定义函数
    for i in range(2, a):  # 任何数%1都会是整数
        if a % i == 0:
            return False#不是素数
    else:  # 在整个循环结束后，if语句都没执行
        return True#是素数

if is_prime(a):
    print(f'{a}是素数')
else:
    print(f'{a}不是素数')