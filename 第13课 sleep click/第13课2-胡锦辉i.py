import random as r#简化random
import turtle as t
import time

#初始化准备
t.hideturtle()
A=[0,1,2,3,4,5,6,7,8,9]#录入单词集合
k='y'
s=''
z=0

def move(x,y,i):#写单词
    t.up()
    t.goto(x,y)
    t.down()
    t.write(i, font=('宋体', 100, 'normal'))

#-----------------进入游戏循环-------------
while k == 'y':
    B = []  # 乱序
    move(-300,-50,'看工作台！\n')
    time.sleep(2)
    t.clear()

    a=int(input('你能记住几位数？'))#记录数字位数
    for i in range(a):
        c = r.randint(0, len(A) - 1)
        B.append(str(A[c]))#B中存储


    #print(B)
    z=int(input('按1并回车开始游戏'))#给予准备时间
    time.sleep(2)

    if z==1:
        for i in range(len(B)):
            t.tracer(False)# -----------加速画面
            move(-20,0,B[i])
            t.tracer(True)
            time.sleep(1)
            t.clear()
            move(-300,-50,'开始记忆')
            time.sleep(2)
            t.clear()
            s+=B[i]#添加数字字符串

        move(-300, -50, '在工作台\n输入数字')
        anwser=input('输入你记忆的数字')
        if anwser==s:
            print('全都答对')
        else:
            print('有错误哟')
    else:
        z = input('输入你记忆的数字')

    #print(A)
    k=input('是否再次记忆？y/n')#再玩一次