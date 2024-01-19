num=int(input('输入水仙花位数'))

for i in range(10**(num-1),10**num):
    judge_num=0
    for j in str(i):
        judge_num+=int(j)**num
    if judge_num==i:
        print(i,'是水仙花数')