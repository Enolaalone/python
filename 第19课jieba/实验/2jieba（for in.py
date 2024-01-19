import jieba#导入结巴库

with (open('data.txt','r',encoding='utf-8') as f):
    a=f.readlines()

print(a)#列表

for i in a:#必须用for in 来提取结巴
    k=jieba.lcut(i,cut_all=False)#精简模式
    print(k)#标点，数字，词语都会单独切出
print()

for i in a:#必须用for in 来提取结巴
    k=jieba.lcut(i,cut_all=True)#全模式，冗杂
    print(k)#标点，数字，词语都会单独切出