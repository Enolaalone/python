print("欢迎进入密室！")
point=input("按0，进入密室")
while True:
    if point=='0':
        point=input('1.进入密室1  2.进入密室2')
    if point=='1':
        print('欢迎进入密室1')
        point=input('4.进入密室4    2.进入密室2  0.返回入口')
    if point=='2':
        print('欢迎进入密室2')
        point=input('3.进入密室3    1.进入密室1     0.返回入口')
    if point=='3':
        print('是个死胡同！')
        point=input('2.返回')
    if point=='4':
        print('偶遇小矮人')
        print('小矮人：我身后就是出口')
        point=input('5.进入   1.返回')
    if point=='5':
        print('一道亮光闪过')
        print('------------------')
        print('恭喜通关！')
        break
    else:
        print('你进入神秘空间')
        point='0'