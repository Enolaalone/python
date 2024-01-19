for i in range(5):
    print('第%d次循环'%(i+1))#后面%（）中的内容会填充%d的内容

print()#
#end=''不转行
for i in range(5):
    print('第%d次循环'%(i+1),end=' ')#end以等号的内容结尾，print自带\n,用end=''去掉