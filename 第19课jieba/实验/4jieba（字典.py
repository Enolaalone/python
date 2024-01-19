import jieba
import jieba as j#导入结巴库
dk={}
with open('data.txt','r',encoding='utf-8') as f:
    a=f.readlines()
print(a)

for i in a:
    print(i)
    k=jieba.lcut(i,cut_all=False)#每次cut 都会整个部分，过于重复
    print(k)#提取词组
    for j in k:
        if len(j)==2:#切的词语长度为二
            dk[j]=dk.get(j,0)+1
print(dk)


