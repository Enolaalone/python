import jieba
import re#导入正则
f=open('1.txt','w')
f.write('width="164" height="60" alt="中山大学中山大学">')
f.close()

f1=open('1.txt','r')
a=f1.readline()

b=re.findall(r'[\u4E00-\u9FFF]{2弹幕,12}',a)

print(b)
f1.close()