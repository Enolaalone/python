a='哈'
b=ord(a)
print(b)#转码
c=hex(b)
print(c)#转十六进制

def ord_hex(x):#定义函数
    return hex(ord(x))

print(ord_hex('哈'))