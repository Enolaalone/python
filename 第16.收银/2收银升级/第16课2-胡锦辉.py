import random
#-------------------基础量导入---------------------------
A=['0','1','2','3','4','5','6','7','8','9']
account1={'100': '01', '101': '02'}#账号
mima1={'100': '123456', '101': '123456'}#密码
thing1={'100': ('台灯', '20元/个'), '101': ('水瓶', '21元/个'), '102': ('画', '22元/个'), '103': ('小零食', '1元/个'), '104': ('笔', '3元/个')}#东西
price1={'100': 20, '101': 21, '102': 22, '103': 1, '104': 3}#价格
num1={'100': 0, '101': 0, '102': 0, '103': 0, '104': 0}#出库基础数量
num2={'100': 1, '101': 1, '102': 1, '103': 1, '104': 1}#入库基础数量

#---------------------------------------进入系统-----------------
print('欢迎来到商店')
while (1):
    verify = ''
    for i in range(4):  # 四位验证码
        a = random.randint(0, 9)
        verify += A[a]  # 生成验证码
    account=input('请输入账号')
    mima=input('请输入密码')
    print('验证码:'+verify)
    test = input('输入验证码' )
    #print(mima1.get(account))
    if (account in account1) and (mima in mima1.get(account)) and (test==verify):#后者检查密码
        print(f'{account1[account]}欢迎登录')
        break
    else:
        print('账号,密码或验证码有错误,再次输入')
        continue

while (1):
    step=input('菜单:按1.商品查询\n\t按2.商品录入\n\t按3.结账\n\t按4.退出')
    if step=='1':
        while (1):
            num = input('输入商品编码')
            if num in thing1:  # 只会检查键是否存在
                print(thing1[num],'x',num2[num])#对象及数量
                break
            else:
                print('没有此商品，再输一次')
                continue
    elif step=='2':
        total = ''
        while (1):  # 编码查重
            num = input('输入商品编码')
            if num in thing1:
                print('编码重复，再输入一次')
                continue
            else:
                num1[num]= 0  # 基础数量录入
                num2[num]=1# 基础数量录入
                #print(num1,'\n',num2,'\n',thing1)
                break

        while (1):
            name = input('输入物品名称')
            if name in thing1.values():  # 判断是否存在重复的值
                print('错误，再输一次')
                continue
            else:
                break
        total += name
        total += ':'
        price = input('输入商品单价')
        total += price
        price1[num]=float(price)# 价格录入
        total += '元/个'
        thing1[num] = total#构建商品信息
        #print(thing1[num])

    elif step=='3':
        money = 0
        A = set()
        while (1):
            num = input('输入商品编码')
            A.add(num)
            if num in thing1:  # 只会检查键是否存在
                print(thing1[num], 'x1')
                num1[num] += 1
                money += price1[num]  # 计算金额
                print(f'总计{money}元')
                k = input('是否继续录入商品？ Enter继续/n')#继续 或 结账
                if k == '':
                    continue
                else: #结账部分，账单
                    for i in A:
                        print(f'{thing1[i]}x{num1[i]}')
                    print(f'总计{money}元')

                    while (1):
                        ma = input('请出示付款码')
                        if len(ma) != 18 or ma[0:2] not in ['10', '12', '11', '13', '14', '15']:
                            print('无效码,再试一次')
                            continue
                        else:
                            print('付款成功')
                            for i in A:
                                print(f'{thing1[i]}x{num1[i]}')
                            print(f'总计{money}元')
                            print('感谢惠顾，欢迎下次光临')
                            break
                    break
            else:
                print('没有此商品，再输一次')
                continue

    elif step=='4':
        break
    else:
        continue




