for j in range(9,0,-1):
    for i in range(1,1+j):
        print("%dx%d=%d"%(i,j,i*j),end='\t')
    print()

for j in range(1,10):
    for i in range(1,j+1):
        print("%dx%d=%d" % (i, j, i * j), end='\t')
    print()