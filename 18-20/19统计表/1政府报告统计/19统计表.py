import Data1
import jieba
from pyecharts.charts import Bar

with open('政府工作报告2021.txt','r',encoding='utf-8') as f:
    Data1.reports_0=f.readlines()
    for i in Data1.reports_0:
        if i!='\n':
            i=i.strip('\n')
            Data1.reports_1.append(i)
    print(Data1.reports_1)

for words in Data1.reports_1:
    list=jieba.cut(words,cut_all=True)
    for word in list:
        if len(word)>=2:
            Data1.words[word]=Data1.words.get(word,0)+1
print(Data1.words)

words_order=sorted(Data1.words.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(words_order)

for i in range(10):
    Data1.words_list_1.append(words_order[i][0])
    Data1.words_list_2.append(words_order[i][1])

Bar().add_xaxis(Data1.words_list_1).add_yaxis('热门词',Data1.words_list_2).render('政府工作报告2021.html')