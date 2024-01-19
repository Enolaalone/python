import random as r
import Data1
def price(n):
    a,b=n.split(':')
    b=b[0:-3]
    return int(b)
print('欢迎来到商店')
while True:
    account=input('输入账号')
    code=input('输入密码')
    if account in Data1.account1 and code==Data1.mima1[account]:
        while True:
            verify=''
            for i in range(4):
                a=r.randint(0,len(Data1.A)-1)
                verify+=Data1.A[a]
            print('验证码：',verify)
            check=input('输入验证码')
            if check==verify:
                break
            else:
                print('验证码错误')
        print(f'{Data1.account1[account]}欢迎登录')
        break
    else:
        print('账号不存在或密错误')

while True:
    a=input('1商品查询  2商品录入   3结账   4退出')
    if a=='1':
        num=input('输入商品编码')
        if num in Data1.thing1:
            print(f'{Data1.thing1[num]}')
        else:
            print('商品不存在')
    if a=='2':
        while True:
            num=input('输入商品编号')
            if num in Data1.thing1:
                print('编号重复')
            else:
                break
        name=input('输入商品名称')
        price0=input('输入商品价格')
        Data1.thing1[num]=f'{name}:{price0}元/个'
        print(Data1.thing1)
    if a=='3':
        while True:
            while True:
                num=input('商品编码')
                if num not in Data1.thing1:
                    print('无此商品')
                else:
                    break
            print(f'{Data1.thing1[num]}x1')
            if Data1.thing1[num] not in Data1.subject:
                Data1.subject[Data1.thing1[num]]=1
            else:
                Data1.subject[Data1.thing1[num]]+=1
            a=input('按Enter继续   按w结账')
            if a=='w':
                money=0
                for key,value in Data1.subject.items():
                    Data1.subject[key]=price(key)*value
                    print(f'{key}   {value}个    共计{Data1.subject[key]}元')
                    money+=Data1.subject[key]
                print(f'总计{money}元')
                break
    if a=='4':
        break


