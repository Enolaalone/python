thing1={'100': ('台灯', '20元/个'), '101': ('水瓶', '21元/个'), '102': ('画', '22元/个'), '103': ('小零食', '1元/个'), '104': ('笔', '3元/个')}
price1={'100': 20, '101': 21, '102': 22, '103': 1, '104': 3}

num1={'100': 0, '101': 0, '102': 0, '103': 0, '104': 0}
money=0
A=set()
while (1):
    num = input('输入商品编码')
    A.add(num)
    if num in thing1:  # 只会检查键是否存在
        print(thing1[num],'x1')
        num1[num]+=1
        money+=price1[num]#计算金额
        k =input('是否继续录入商品？ Enter继续/n')
        if k=='':
            continue
        else:
            for i in A:
                print(f'{thing1[i]}x{num1[i]}')
            print(f'总计{money}元')
            break
    else:
        print('没有此商品，再输一次')
        continue