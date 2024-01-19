a={'111': ['ji', '100元']}

num=input('输入商品编码')
if num in a:#只会检查键是否存在
    print(a[num])
else:
    print('错误，再输一次')
#-------------------查询
