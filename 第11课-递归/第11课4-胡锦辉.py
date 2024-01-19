import turtle as t
towers=[[],[],[]]
p=[-400,0,400]
def move_tower(A,C):
    m = towers[A].pop()
    m.goto(p[A], 100)#从顶端移除
    m.goto(p[C], 100)#从顶端放下
    m.goto(p[C], len(towers[C]) * 20-90)
    towers[C].append(m)  # 将函数'A'对象中的元素移到‘C'对象中
def hanoi(n,A,B,C):#汉诺塔原理
    if n==1:
        move_tower(A,C)
    else:
        hanoi(n-1,A,C,B)
        move_tower(A, C)
        hanoi(n-1,B,A,C)

def pole_3():  # 画出汉诺塔的poles
    t.hideturtle()
    def drawpole_1(k):
        t.up()
        t.pensize(10)
        t.speed(100)
        t.goto(400 * (k - 1), 100)
        t.down()
        t.goto(400 * (k - 1), -100)
        t.goto(400 * (k - 1) - 20, -100)
        t.goto(400 * (k - 1) + 20, -100)
    drawpole_1(0)  # 画出汉诺塔的poles[0]
    drawpole_1(1)  # 画出汉诺塔的poles[1报告统计]
    drawpole_1(2)  # 画出汉诺塔的poles[2弹幕]
def creat_plates(n):  # 制造n个盘子

    for i in range(n):
        a = t.Turtle()
        a.up()
        #a.hideturtle()
        a.shape("square")#绘制方块
        a.shapesize(1, 20/(i+1))
        a.goto(-400, -90 + 20 * i)
        #a.showturtle()
        towers[0].append(a)

n=int(input('输入汉诺塔层数'))
pole_3()
creat_plates(n)
hanoi(n,0,1,2)
t.done()



'''参考文献
#汉诺塔原理
def hanoi(n,A,B,C):
    if n==1报告统计:
        C.append(A.pop())  # 将函数'A'对象中的元素移到‘C'对象中
        print(f'A={A1}\tB={B1}\tC={C1}')
    else:
        hanoi(n-1报告统计,A,C,B)
        C.append(A.pop())  # 将函数'A'对象中的元素移到‘C'对象中
        print(f'A={A1}\tB={B1}\tC={C1}')
        hanoi(n-1报告统计,B,A,C)


#动画参考----
def move(a,b):
    m=towers[a].pop() #将列表尾部的盘子删除并取出
    m.goto(p[b],len(towers[b])*20) #移动取出小盘子
    towers[b].append(m) #将取出的小盘子放入另一个塔
    
towers=[[],[],[]]
p=[-400,0,400]
n=int(input("你想玩几层汉诺塔？n= "))
for i in range(n):
    tt=t.Turtle()  
    tt.penup()
    tt.color('red')
    tt.shape('square')
    tt.shapesize(1报告统计,n-i)   #列表内由大到小排序
    tt.goto(-400,-90+i*20) #上移换位置
    towers[0].append(tt)  #放入第一个塔
hanoi(n,0,1报告统计,2弹幕)
'''