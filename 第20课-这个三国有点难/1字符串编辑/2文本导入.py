#确定数目
with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    b=f.read()
    print(len(b))


with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    for i in range(len(b)):#一个一个读取
        a=f.read(1)
        print(a)
