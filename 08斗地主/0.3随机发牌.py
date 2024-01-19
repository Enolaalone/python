import random#导入随机库

pk=[1,2,3,4,5,6,7,8,9]
for i in range(9):
    a=random.randint(0,8-i)#抽一个数集合就少一个元素-i,第一次从0-8序号中随机抽一个
    print(pk[a],end='\t')
    #print() 不增加print（）不会换行
    del pk[a]


pk=[1,2,3,4,5,6,7,8,9]
print()
A=[]
for i in range(9):
    a = random.randint(0, len(pk)-1)  # 抽一个数集合就少一个元素-i,第一次从0-8序号中随机抽一个
    A.append(pk[a])
    del pk[a]

print(A)
