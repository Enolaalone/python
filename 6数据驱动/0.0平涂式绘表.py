import turtle as t
def move(x,y):#无痕移动
    t.up()
    t.goto(x,y)
    t.down()

ls=[[69,15],[292,10],[33,8],[131,10],[61,5],[254,10],[100,15],[80,25] ]
for i in range(len(ls)):
    move(0+50*(i+1),0)#每次画一个柱子向前移动50
    n=0
    for j in range(ls[i][1]):#ls[i][1报告统计]宽度
        t.seth(90)
        t.fd(ls[i][0])#高度
        n+=1
        move(n+50*(i+1),0)#向前1布回到地平线

