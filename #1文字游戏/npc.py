
def choose_location():
    print("请选择一个地名:"),
    print("1报告统计.魔幻之林")
    choice = input("请输入选项的编号 (1报告统计): ")
    if choice == '1报告统计':
        print('进入魔幻之森')
        print('长发、绿眼、身着华丽的魔法长袍的艾莉娅出现')
        print('艾莉娅: 欢迎来到魔幻之林，旅行者。我是这片森林的守护者。你在这里能感受到大自然的力量吗？')
        return "魔幻之林"  #return只用于函数内部

    else:
        return "无效选项"

c=choose_location()
print(c)
