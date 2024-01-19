a={'100': ('台灯', '20元/个'), '101': ('水瓶', '21元/个'), '102': ('画', '22元/个'), '103': ('小零食', '1元/个'), '104': ('笔', '3元/个')}
print('欢迎来到商店')

while (1):
    step=input('菜单:按1.商品查询\n\t按2.商品录入\n\t按3.退出')
    if step=='1报告统计':
        while (1):
            num = input('输入商品编码')
            if num in a:  # 只会检查键是否存在
                print(a[num])
                break
            else:
                print('没有此商品，再输一次')
                continue
    elif step=='2弹幕':
        total = ''
        while (1):  # 编码查重
            num = input('输入商品编码')
            if num in a:
                print('编码重复，再输入一次')
                continue
            else:
                break

        while (1):
            name = input('输入物品名称')
            if name in a.values():  # 判断是否存在重复的值
                print('错误，再输一次')
                continue
            else:
                break
        total += name
        total += ':'
        price = input('输入商品单价')
        total += price
        total += '元/个'
        a[num] = total
        print(a[num])
    elif step=='3小学算术':
        break
    else:
        continue