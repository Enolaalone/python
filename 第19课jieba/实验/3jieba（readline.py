import jieba
import jieba as j#导入结巴库
dk={}
with open('data.txt','r',encoding='utf-8') as f:
    a=f.readline()
    print(a)

'''for i in a:
    k=jieba.lcut(a,cut_all=True)#每次cut 都会整个部分，过于重复
    print(k)'''

