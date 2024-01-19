strips = ['【', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
text_1 = []

C=open('原文.txt','w')
with open('论语解读版本.txt','r',encoding='utf-8') as f:
    text_0=f.readlines()
for sentence in text_0:
    if sentence[2:3] in strips or sentence=='\n':
        continue
    else:
        for i in strips:
            sentence=sentence.replace(i,'')
        C.write(sentence)
C.close()
