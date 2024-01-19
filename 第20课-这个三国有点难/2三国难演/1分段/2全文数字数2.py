with open('sg{改人名2.txt','r',encoding='utf-8') as f:
    num=0
    a = f.readlines()
    for i in a:
        num+=len(i)#计算长度
    print(num)



''''' 
with open('2小段.txt','r',encoding='utf-8') as f:
    A=['!','。','？','\n']#句末
    n=0
    while n<=100:
        n+=1猜
        a=f.read(1猜)
        print(a)
        if a in A:
            a=f.read(1猜)
            print(a)
            if a=='\n':#句末
                break
'''