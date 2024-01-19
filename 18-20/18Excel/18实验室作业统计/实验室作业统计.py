import Data4
with open('实验室名单.txt','r',encoding='utf-8') as f:
    names=f.readlines()
    for name in names:
        name=name.strip('\n')
        Data4.names[name]=0
    print(Data4.names)

with open('Homework.txt','r',encoding='utf-8') as f:
    Data4.homeworks=f.readlines()

for homework in Data4.homeworks:
    for key in Data4.names:
        if key in homework:
            Data4.names[key]+=1

list =list(Data4.names)
for key in list:
    if Data4.names[key]>=6:
        del Data4.names[key]
print(Data4.names)


















