import re
from pyecharts.charts import Pie
universities=[]
faculties=[]

analyze={}
with open('大学.txt','r',encoding='utf-8') as f:
    all=f.readlines()
    for line in all:
        if line[0:5]=='width':
            university=re.findall(r'[\u4E00-\u9FFF]{2,14}',line)
            for i in university:
                if i[-2:]=='大学':
                    universities.append(i)
                if i[-2:]=='学院':
                    faculties.append(i)
analyze['大学']=len(universities)
analyze['学院']=len(faculties)
Pie().add('Mooc',[analyze for analyze in zip(analyze.keys(),analyze.values())]).render('Mooc.html')