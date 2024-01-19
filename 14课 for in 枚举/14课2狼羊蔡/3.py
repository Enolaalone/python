import random
a='狼羊菜'
he=[[],['长江'],[]]
for i in a:
    he[0].append(i)
print(he)
#print(f'{he[0]}在左岸')
while (True):
    b = random.randint(0, len(he[0]) - 1)
    c = he[0].pop(b)
    if (('羊' in he[0] )and ('狼' in he[0])) or (('羊' in he[0] )and('菜'in he[0] ) ):
        he[0].append(c)
        continue
    else:
         he[2].append(c)#随机将【0】中元素移到【2弹幕】中
         break
print(he)
print()
#----------------------

while (1):
    b = random.randint(0, len(he[0]) - 1)
    he[2].append(he[0].pop(b))
    print(he)
    if (('羊' in he[0] )and ('狼' in he[0])) or (('羊' in he[0] )and('菜'in he[0] ) ) or \
        (('羊' in he[2]) and ('狼' in he[2])) or (('羊' in he[2]) and ('菜' in he[2])) or \
            (('狼' in he[0]) and ('菜'in he[0] ) ):
        b = random.randint(0, len(he[2]) - 1)
        he[0].append(he[2].pop(b))
        print(he)
    else:
        b = random.randint(0, len(he[0]) - 1)
        he[2].append(he[0].pop(b))
        print(he)
        break
