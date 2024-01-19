import jieba
from pyecharts.charts import Bar
b={}#空字典
#---------文件 读取----------------------
with open('政府工作报告2021.txt','r',encoding='utf-8') as f:
    a=f.readlines()

for i in a:
    k=jieba.lcut(i,cut_all=True)#精简模式
#一行一行读取
#print(k)  # 检测
    for j in k:
        if len(j)==2:#排除标点
            b[j]=b.get(j,0)+1#无则创建，有则加一
print(b)#检测字典
#---------------------------------------------------------------
dp=list(b.items())#转为列表比较
print(dp)
#-------------------------------------------------------------------
dp.sort(key=lambda c:c[1],reverse=True)#降序，根据元组二号元素排序
print(dp)
b={}
for i in dp:#重构列表
    b[i[0]]=i[1]
print(b)
#-----------------------------------------------------------------------------------
lis1=list(b.keys())
lis2=list(b.values())

Bar().add_xaxis(lis1).add_yaxis('两字高频词',lis2).render('《政府工作报告2021》.html')

