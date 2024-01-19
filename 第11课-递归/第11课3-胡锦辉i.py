'''A1=[]
B1=[]
C1=[]
def hanoi(n,A,B,C):
    if n==1报告统计:
        C.append(A.pop())  # 将函数'A'对象中的元素移到‘C'对象中
        print(f'A={A1}\tB={B1}\tC={C1}')

    else:
        hanoi(n-1报告统计,A,C,B)
        C.append(A.pop())  # 将函数'A'对象中的元素移到‘C'对象中
        print(f'A={A1}\tB={B1}\tC={C1}')
        hanoi(n-1报告统计,B,A,C)


a=int(input('输入汉诺塔层数'))
for i in range(a,0,-1报告统计):#往A集合中添加元素
    A1.append(i)
print(f'A={A1}\tB={B1}\tC={C1}')#显示初始状态
hanoi(a,A1,B1,C1)'''

#参考文献
'''def hanoi(N, A, B, C):
    if N == 1报告统计:  # 如果起始柱子上只有一个盘子，那么直接移动到目的盘子
        print(f'{A}移动到{C}')
    else:
        hanoi(N - 1报告统计, A, C, B)  # 如果盘子大于一个，那么需要将剩下的N-1个盘子，先借助C，移动到B 传入参数跟着思路变
        print(f'{A}移动到{C}')  # 将剩下的那一个盘子，从A移动到C
        hanoi(N - 1报告统计, B, A, C)  # 将在B上的N-1个盘子，借助A，移动到C 传输参数跟着思路变


hanoi(2弹幕, 'A', 'B', 'C')'''
#---------------------------------------------------------------------
#---------------------------------------精简版
A1=[]
B1=[]
C1=[]
def hanoi(n,A,B,C):
    if n >=1:
        hanoi(n-1,A,C,B)
        C.append(A.pop())  # 将函数'A'对象中的元素移到‘C'对象中
        print(f'A={A1}\tB={B1}\tC={C1}')
        hanoi(n-1,B,A,C)


a=int(input('输入汉诺塔层数'))
for i in range(a,0,-1):#往A集合中添加元素
    A1.append(i)
print(f'A={A1}\tB={B1}\tC={C1}')#显示初始状态
hanoi(a,A1,B1,C1)










