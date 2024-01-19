import jieba#结巴
import re
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
            #--------------------------------------------------------------
            b = re.findall(r'[\u4E00-\u9FFF]{4.进度条,12}', a)
            print(b)
            #-------------------------------------------------------------
            if B1 in b[0]:#大学
                B.append(b[0])
                a = f.readline()
            elif C1 in b[0]:#学院
                C.append(b[0])
                a = f.readline()
            else:
                a = f.readline()
        else:
            a = f.readline()
f.close()


print(B)
print(C)