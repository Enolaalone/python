import random as r
import Data1


def price(n):
    a, b = n.split(':')
    b = b[0:-3]
    return int(b)


def read():
    f = open('商品.txt', 'r')
    Data1.thing = {}
    a = f.readlines()
    for i in a:
        i = i.strip('\n')
        t1, t2, t3 = i.split(':')
        Data1.thing[t1] = f'{t2}:{t3}'
    f.close()


def record():
    f = open('商品.txt', 'w')
    for key, value in Data1.thing.items():
        f.write(f'{key}:{value}\n')
    f.close()


def change(n, num):
    a, b = n.split(':')
    if num == 1:
        a = input('输入商品名称')
        a += f':{b}'
        return a
    if num == 2:
        b = input('输入修改价格')
        a += f':{b}元/个'
        return a


def change_plus(n):
    while True:
        num = input('输入商品编码')
        if num not in Data1.thing:
            print("商品不存在")
        else:
            break
    Data1.thing[num] = change(Data1.thing[num], n)
    print(Data1.thing)


def bill():
    f = open('账单.txt', 'w')
    money = 0
    for key, value in Data1.subject.items():
        Data1.thing[key] = price(key) * value
        f.write(f'{key}     {value}个    共计{Data1.subject[key]}元\n')
        money += Data1.subject[key]
    f.write(f'总计{money}元\n')
    f.close()


print('欢迎来到商店')
while True:
    account = input('输入账号')
    code = input('输入密码')
    if account in Data1.account1 and code == Data1.mima1[account]:
        while True:
            verify = ''
            for i in range(4):
                a = r.randint(0, len(Data1.A) - 1)
                verify += Data1.A[a]
            print('验证码', verify)
            check = input('输入验证码')
            if check == verify:
                break
            else:
                print('验证码错误')
        print(f'{Data1.account1[account]}欢迎登录')
        break
    else:
        print('账号或密码错误')

while True:
    a = input('1商品查询      2商品录入   3删除商品   4修改商品   5结账     6退出')
    if a=='1':
        read()
        print(Data1.thing)
        num=input('输入商品编码')
        if num in Data1.thing:
            print(f'{Data1.thing[num]}')
        else:
            print('商品不存在')
    if a=='2':
        read()
        while True:
            while True:
                num=input('输入商品编码')
                if num in Data1.thing:
                    print('商品已经存在')
                else:
                    break
            name=input('输入商品名称')
            price0=input('商品价格')
            Data1.thing[num]=f'{name}:{price0}元/个'
            print(Data1.thing)
            a=input('Enter继续输入  w退出')
            if a=='w':
                record()
                break
    if a=='4':
        read()
        while True:
            b=input('1修改商品名称    2修改价格')
            print(Data1.thing)
            if b=='1':
                change_plus(1)
                a=input('Enter继续输入  w退出')
                if a=='w':
                    record()
                    break
            if b=='2':
                change_plus(2)
                a=input('Enter继续输入  w退出')
                if a=='w':
                    record()
                    break
    if a=='3':
        read()
        while True:
            while True:
                num=input('商品编码')
                if num not in Data1.thing:

                    print('商品不存在')
                else:
                    break
            del Data1.thing[num]
            print(Data1.thing)
            a=input('Enter继续删除  w退出')
            if a=='w':
                record()
                break
    if a=='5':
        read()
        while True:
            while True:
                num=input('商品编码')
                if num not in Data1.thing:
                    print('无此商品')
                else:
                    break

            print(f'{Data1.thing[num]}x1')
            if Data1.thing[num] not in Data1.subject:
                Data1.subject[Data1.thing[num]]=1
            else:
                Data1.subject[Data1.thing[num]]+=1
            a=input('Enter继续    w结账')
            if a=='w':
                bill()
                break
    if a=='6':
        break



