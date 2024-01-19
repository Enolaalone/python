a={}
num = input('输入商品编码')
total=''
name = input('输入物品名称')
total+=name
total+=':'
price = input('输入商品单价')
total+=price
total += '元/个'
a[num] = total
print(a[num])
