
#\n转行
print('555566666 \n 888888888')

#--------地方切换--------
point=0
#if point==0:
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

