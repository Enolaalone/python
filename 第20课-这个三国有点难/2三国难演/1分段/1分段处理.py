with open('2小段(整段.txt','r',encoding='utf-8') as f:
    A=['!','。','？','\n']#句末
    n=0
    a1=''
    while True:
        n+=1
        a=f.read(1)#一个一个字符的读
        a1+=a
        print(a)
        if a in A:
            a=f.read(1)
            print(a)
            if a=='\n':#句末
                break
    print(a1)#完整一段