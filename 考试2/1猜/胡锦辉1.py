import random

# --------------------------

k = 'y'
while k == 'y':
    a = random.randint(1, 99)
    print(a)
    n = 0

    while True:
        n += 1
        print(n)

        if n > 9:
            print('太笨了，游戏失败')
            break
        num = int(input('猜一个数1-99'))

        if num > a and n <= 9:
            print('大了')
        elif num < a and n <= 9:
            print('小了')
        elif num == a:
            if n <= 3:
                print('猜对了')
                print('A')
                break
            elif 3 < n < 6:
                print('猜对了')
                print('B')
                break
            elif 6 <= n <= 7:
                print('猜对了')
                print('C')
                break
            elif 8 <= n <= 9:
                print('猜对了')
                print('D')
                break
    k = input('是否再玩一次？y/n')
