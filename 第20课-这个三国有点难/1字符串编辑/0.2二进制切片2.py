A='13!@#$%^&国aA'#使用字符串
def jie(a):
    num=(len(a)-2)%8#看和一字节差几位
    #print(num)
    a1,a2=a.split('b')
    #print(a1,a2)
    a1+='b'#还原0b前缀
    for i in range(8-num):#补充成整字节
        a1 += '0'
    a=a1+a2
    return a

a='0b0011'

def jie_1(a):
    return ((len(jie(a))-2)/8)

print(jie_1(a))
