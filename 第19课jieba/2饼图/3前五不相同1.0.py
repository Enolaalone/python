import jieba
from pyecharts.charts import Bar
def report(name):
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
    return b

def shi(dic,num):
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



bing1=shi(dic2021,5)
bing2=shi(dic2022,5)
#------------------------------------

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
print(bing4)#呈现比例