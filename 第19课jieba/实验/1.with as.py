f=open('with.txt','w')#创建文件
f.write('123456\n654321')
f.close()

#===============================================================
with open('with.txt','r',encoding='utf-8') as f:#打开文件后直接关闭
    a=f.readline()#对文件的操作直接放后面
    
with open('with.txt', 'r', encoding='utf-8') as f:  # 打开文件后直接关闭
    b=f.readlines()#打印列表
print(a)
print(b)

