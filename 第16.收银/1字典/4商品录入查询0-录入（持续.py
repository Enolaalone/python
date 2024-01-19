a={}
k='y'
while k=='y':
    num=input('输入商品编码')
    name=input('输入物品名称')
    price=input('输入商品单价')
    price+='元/个'
    a[num]=name,price
    print(a)
    k=input('是否再次录入？ y/n')