#单元素

A=['a']
B=[]
C=[]
print(A)
for i in A:#依次取出A中的元素赋给i  遍历循环
   print(i)

   b= ord(i)#取A中元素的ASCII值
   print(b)

   c=ord(i)+3#凯撒密码+3小学算术
   print(c)

   B.append(c)#c的值赋给B集合
   print(B)

for j in B:#依次取出B中元素
    print(j)

    d=chr(j-3)#解码
    print(d)

    C.append(d)
    print(C)