#-----------------------------------------------------------------------------------------------------------------------
import jieba
from pyecharts.charts import Pie,Page#page实现多图一网页
def report(name):#切词，字典排序
    b={}#空字典
    #---------文件 读取----------------------
    with open(f'{name}.txt','r',encoding='utf-8') as f:
        a=f.readlines()

    for i in a:
        k=jieba.lcut(i,cut_all=True)#精简模式
    #一行一行读取
    #print(k)  # 检测
        for j in k:
            if len(j)==2:#排除标点
                b[j]=b.get(j,0)+1#无则创建，有则加一
    #print(b)#检测字典
    #---------------------------------------------------------------
    dp=list(b.items())#转为列表比较
    #print(dp)
    #-------------------------------------------------------------------
    dp.sort(key=lambda c:c[1],reverse=True)#降序，根据元组二号元素排序
    #print(dp)
    b={}
    for i in dp:#重构列表
        b[i[0]]=i[1]
    return b

def shi(dic,num):#提取列表前
    bing1={}#相同项
    n=0
    for key,value in dic.items():
        # print(key)
        if  n<=num-1:
            bing1[key]=value
            n+=1
    return bing1
#---------------------------------相同前十
dic2021=report('政府工作报告2021')
dic2022=report('政府工作报告2022')

#----------------------------前十相同--------------------------------
bing1=shi(dic2021,10)
bing2=shi(dic2022,10)


bing3_1={}#统计前10公共
bing3_2={}
for key,value in bing1.items():
    #print(key)
    if key in bing2:
        bing3_1[key]=value
        bing3_2[key]=bing2[key]

#print(bing3_1)
#print(bing3_2)
#-----------------------------------前五不同-----------------------------------
bing1=shi(dic2021,5)
bing2=shi(dic2022,5)

bing4={}#统计前5不同
for key,value in bing1.items():
    #print(key)
    if key not in bing2:
        bing4[key]=value
#print(bing4)#呈现比例
for key,value in bing2.items():
    #print(key)
    if key not in bing1:
        bing4[key]=value
#print(bing4)#呈现比例

#-----------------------------------------------------------------------------------------------------------------------
page=Page()#创建空网页
pie1=Pie().add('前十相同2021',[bing3_1 for bing3_1 in zip(bing3_1.keys(),bing3_1.values())])
pie2=Pie().add('前十相同2022',[bing3_2 for bing3_2 in zip(bing3_2.keys(),bing3_2.values())])
pie3=Pie().add('前五不同',[bing4 for bing4 in zip(bing4.keys(),bing4.values())])
page.add(pie1,pie2,pie3).render('数据比较.html')
