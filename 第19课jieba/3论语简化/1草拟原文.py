import jieba#
f=open('论语解读版本.txt','r',encoding='utf-8')

f2=open('原文.txt','w')

A=['【','】','1猜','2弹幕','3小学算术','4.进度条','5','6','7','8','9','0','(',')','/','_']#不符合规范的开头

#print(f.readlines())

a = f.readline()
while a!='':#一行一行读取判断是否是原文
    if a=='\n':#空行跳过
        a = f.readline()
    else:
        if a[2:3] not in A:#规范
            f2.write(a)
            a = f.readline()
        else:
            a = f.readline()
f2.close()
f.close()


