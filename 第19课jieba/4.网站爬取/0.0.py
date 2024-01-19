f=open('1.txt','w')
f.write('width="164" height="60" alt="中山大学">')
f.close()

f1=open('1.txt','r')
a=f1.readline()
print(a)
f1.close()