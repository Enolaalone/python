print('游戏开始英雄登场')
hero_name=input('请输入英雄姓名')

#-------性别-------
a=1
while a>=1:
    hero_gender = input('请输入英雄性别，男/女')
    if hero_gender == '男':
        print('欢迎你，我的' + hero_name, '勇士')
        break
    if hero_gender == '女':
        print('欢迎你，我的' + hero_name, '女神')
        break
    else:
        print('请重新选择')#再次选择
        a+=1

#--------年龄-----------
old=int(input('How old are you?'))
if old>=20:
    print('呀！老江湖')
else:
    print('少年！初出茅庐少年英雄')

#-------开始游戏----------
print('欢迎来到江湖（游戏开始）\n      进入世界')#使用\n换行
a=1
t=input('A.进入1教  B.进入2教')
while a>=1:
    if t=='A':
        print('走进1教')
        t = input(' B.进入2教  C.退出')
        if t=='C':
           break
        else:
            a+=1

    elif t=='B':
        print('进入2教')
        t=input('A.进入1教  C.退出')
        if t=='C':
           break
        else:
            a+=1
    else:
        print('程序错误，游戏结束')
        break
