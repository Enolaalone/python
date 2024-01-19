a={'111': ['ji', '100元']}
while (1):
    num=input('输入商品编码')
    if num in a:#只会检查键是否存在
        print(a[num])
        break
    else:
        print('错误，再输一次')
        continue
#-------------------查询
