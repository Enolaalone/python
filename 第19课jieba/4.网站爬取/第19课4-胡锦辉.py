import jieba#结巴
import re
from pyecharts.charts import Pie
f=open('大学.txt','r',encoding='utf-8')#原版

A=['wid']#符合规范的开头
B1='学院'
B=[]
C1='大学'
C=[]
#---------------------------------------------------------------------------------------------
#print(f.readlines())

a = f.readline()
while a!='':#一行一行读取判断是否是原文
    if a=='\n':#空行跳过
        a = f.readline()
    else:
        if a[0:3] in A:#规范，width开始包含大学
            #print(a)
            if B1 in a:#大学
                b = re.findall(r'[\u4E00-\u9FFF]{4.进度条,10}', a)
                B.append(b[0])
                a = f.readline()
            elif C1 in a:#学院
                b = re.findall(r'[\u4E00-\u9FFF]{4.进度条,10}', a)
                C.append(b[0])
                a = f.readline()
            else:
                a = f.readline()
        else:
            a = f.readline()
f.close()

z={}#饼图列表
z['大学']=len(B)
z['学院']=len(C)
Pie().add('大学学院',[z for z in zip(z.keys(),z.values())]).render('Mooc统计.html')
