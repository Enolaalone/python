import random as r

k='y'
while k=='y':
    num=r.randint(1,100)
    n=0
    while True:
        n+=1
        a=int(input('输入猜的数'))
        if n>9:
            print('游戏失败')
            break

        if a<num:
            print('小了')
        if a>num:
            print('大了')
        if a==num:
            print('恭喜猜中')
            if n<=3:
                print("A")
                break
            if 3<n<=6:
                print('B')
                break
            if 6<n<=9:
                print('C')
                break

    k=input('是否重玩一次？y/n')