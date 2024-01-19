import re
import jieba
import Data

C={'答':'曰','云':'曰','谓':'曰','语':'曰','道':'曰','议':'曰','说':'曰','喊':'曰','叫':'曰','问':'曰',}
with open('人物3.txt','r',encoding='utf-8') as f :
    A=f.readlines()
    people_names={}
    people_say_times={}
    for i in range(len(A)):
        if A[i]=='\n':
            continue
        else:
            A[i]=A[i].strip(' \n')
            person=A[i].split('字')
            people_names[person[0]]=person[1]
            people_say_times[person[0]]=0
    people_say_words=people_say_times.copy()

with open('sg（原文）utf-8.txt','r',encoding='utf-8') as f:
    f0=open('原文改人名.txt','w',encoding='utf-8')
    for sentence in f:
        for key, value in C.items():
            sentence=sentence.replace(key,value)
        for key,value in people_names.items():
            sentence=sentence.replace(value,key)
        for key,value in Data.problem.items():
            sentence=sentence.replace(key,value)
        f0.write(sentence)
    f0.close()

with open('原文改人名.txt','r',encoding='utf-8') as f:
    for i in range(7500):
        names=[]
        sentence=''
        word=''

        while True:
            word=f.read(1)
            sentence+=word
            if word=='曰':
                i=f.read(2)
                if i=='："':
                    break

        key_sentence=re.findall(r'(.{0,15})(曰)',sentence)
        for i in range(len(key_sentence)):
            key_list=jieba.lcut(key_sentence[i][0],cut_all=True)
            for name in key_list:
                if name in people_names:
                    people_say_times[name]+=1
                    names.append(name)

        words=''
        while word!='"':
            word=f.read(1)
            words+=word
        for name in names:
            people_say_words[name]+=len(words)

max_times=sorted(people_say_times.items(),key=lambda x:(x[1],x[0]),reverse=True)
max_words=sorted(people_say_words.items(),key=lambda x:(x[1],x[0]),reverse=True)
print(max_words)
print(max_times)







