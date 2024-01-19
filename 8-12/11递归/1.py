import turtle as t

towers=[[],[],[]]
p=[-400,0,400]

def move_tower(a,c):
    m=towers[a].pop()
    m.goto(p[a],100)
    m.goto(p[c],100)
    m.goto(p[c],len(towers[c])*20-90)
    towers[c].append(m)

def hanoi(n,a,b,c):
    if n==1:
        move_tower(a,c)
    else:
        hanoi(n-1,a,c,b)
        move_tower(a,c)
        hanoi(n-1,b,a,c)

def draw_pole(k):
    t.hideturtle()
    t.pu()
    t.pensize(10)
    t.goto(p[2]*(k-1),100)
    t.pd()
    t.goto(p[2]*(k-1),-100)
    t.goto(p[2]*(k-1)+20,-100)
    t.goto(p[2]*(k-1)-20,-100)

def create_place(n):
    k=n
    for i in range(n):
        a=t.Pen()
        a.pu()
        a.shape('square')
        a.shapesize(1,2*k)
        a.goto(p[0],-90+20*i)
        towers[0].append(a)
        k-=1

n=int(input('汉诺塔层数'))

for i in range(3):
    draw_pole(i)

create_place(n)
hanoi(n,0,1,2)
t.done()