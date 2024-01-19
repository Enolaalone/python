print('欢迎进入密室逃脱')
point = input('按0.进入入口')
while True:

    if point=='0':
        point=input('1.进入密室1\t2.进入密室2')
    if point=='1':
        print('欢迎来到密室1')
        point=input('按4.进入密室4\t按2.进入密室2\t按0.返回入口')
    if point=='2':
        print('欢迎来到密室2')
        point=input('按3.进入密室3\t按1.进入密室1\t按0.返回入口 ')
    if point=='4':
        print('偶遇小矮人')
        print('小矮人：“我身后的门通往出口')
        point=input('你的选择是：按5听话进门 \t按1返回密室1')
    if point=='3':
        print('哎呀！是个死胡同')
        point=input('按2返回')
    if point=='5':
        print('眼前一道光闪过你到达入口')
        print('------------')
        print('恭喜通过！')
        break
    else:
        print("你进入神秘空间\n传送中...")
        point='0'