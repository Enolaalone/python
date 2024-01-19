a={'123':'jjj'}
total=''
while (1):#编码查重
    num = input('输入商品编码')
    if num in a:
        print('编码重复，再输入一次')
        continue
    else:
        break

while (1):
    name = input('输入物品名称')
    if name in a.values():#判断是否存在重复的值
        print('错误，再输一次')
        continue
    else:
        break
total+=name
total+=':'
price = input('输入商品单价')
total+=price
total += '元/个'
a[num] = total
print(a[num])
