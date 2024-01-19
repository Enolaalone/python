
for j in range(9):
    for i in range(j+1):
        print("%dx%d=%d"%(i+1,j+1,(i+1)*(j+1)),end='\t')#\t表示Tab，大空格
    print()#每次for in 循环结束后转行

print()

for j in range(9,0,-1):#{[start,stop),step},-1反步长----j[9,1报告统计]
    for i in range(1,j+1):#---------------------------i[1报告统计,j]
          print('%dx%d=%d'%(i,j,j*i),end='\t')
    print()