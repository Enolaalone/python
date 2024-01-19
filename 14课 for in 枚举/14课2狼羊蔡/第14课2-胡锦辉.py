import random
a=['狼','羊','菜']
he=[[],['长江'],[]]
for i in range(len(a)):#往he 中添加元素
    b = random.randint(0, len(a)-1)
    he[0].append(a.pop(b))
print(he)

while (True):#让计算机明白让羊先过河
    b = random.randint(0, len(he[0]) - 1)
    c = he[0].pop(b)
    if (('羊' in he[0] )and ('狼' in he[0])) or (('羊' in he[0] )and('菜'in he[0] ) ):#让羊先过河
        he[0].append(c)
        continue
    else:
         he[2].append(c)#随机将【0】中元素移到【2弹幕】中
         break
print(he)
#--------------------------------------
while (1):#之后让计算机随机移动一个元素，满足狼和菜在右岸
    he[2].append(he[0].pop(0))
    print(he)
    if (('羊' in he[0] )and ('狼' in he[0])) or (('羊' in he[0] )and('菜'in he[0] ) ) or \
        (('羊' in he[2]) and ('狼' in he[2])) or (('羊' in he[2]) and ('菜' in he[2])) or \
            (('狼' in he[0]) and ('菜'in he[0] ) ):
        he[0].append(he[2].pop(0))
        print(he)
    else:#满足上述条件后，只要把羊从左岸到右岸即可
        he[2].append(he[0].pop(0))
        print(he)
        break
