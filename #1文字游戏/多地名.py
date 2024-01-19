#--------选择地方---------
def time_slow(x):#减慢程序运行速度
    import time
    time.sleep(x)
def choose_location():
    while (1):
        print("请选择一个地名:")
        print("1报告统计.魔幻之林")
        print("2弹幕.幻境之门")
        print("3小学算术.幽灵之谷")
        print("4.进度条.仙境之地")
        print("5.神秘之海")
        print("6.末世之境")
        print("7.结束")
        choice = input("请输入选项的编号 (1报告统计-7): ")
        if choice == '1报告统计':
            print('进入魔幻之森')
            print('长发、绿眼、身着华丽的魔法长袍的艾莉娅出现')
            print('艾莉娅: 欢迎来到魔幻之林，旅行者。我是这片森林的守护者。你在这里能感受到大自然的力量吗？')
            time_slow(3)
            return "魔幻之林"
        elif choice == '2弹幕':
            print('进入幻境之门')
            print('身材高大、戴着神秘的面具、佩戴银色披风的奥林斯出现')
            print('奥林斯: 你好，旅行者。这个幻境之门连接着无数不同的世界，从魔法王国到未来科技世界。但只有被允许的人才能穿越。')
            time_slow(3)
            return "幻境之门"
        elif choice == '3小学算术':
            print('进入幽灵之谷')
            print('眼中流露着悲伤的目光的艾莉斯出现')
            print('艾莉斯: 你好，旅行者。这里是幽灵之谷，被诅咒的地方。我的使命是帮助那些失落的灵魂找到安宁。')
            time_slow(3)
            return "幽灵之谷"
        elif choice == '4.进度条':
            print('进入仙境之地')
            print('穿着流动的仙袍的亚莉亚出现')
            print('亚莉亚: 欢迎来到仙境之地，旅行者。我是这片土地的女神使者。你在这里会感受到和平与祥和。')
            time_slow(3)
            return "仙境之地"
        elif choice == '5':
            print('进入神秘之海')
            print('眼睛中闪烁着深邃的海克特出现')
            print('海克特: 欢迎来到神秘之海，旅行者。我是这片海洋的守护者。它包含了无数秘密。')
            time_slow(3)
            return "神秘之海"
        elif choice == '6':
            print('进入末世之境')
            print('目光坚定的阿尔德里奇出现')
            print('阿尔德里奇: 你好，勇敢的旅行者。这是末世之境，最后的堡垒。在这里，我们守护着最后的希望。')
            time_slow(3)
            return "末世之境"
        elif choice == '7':
            return'7'
        else:
            print('无效')
# 调用函数来获取用户选择的地名
while(1):
    select= choose_location()
    if select=='7':
        break
    else:
        print(select)# 打印用户选择的地名


