import jieba
f=open('1.txt','w')
f.write('width="164" height="60" alt="中山大学">')
f.close()

f1=open('1.txt','r')
a=f1.readline()
k=jieba.lcut(a,cut_all=False)
print(k)
f1.close()