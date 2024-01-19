import math
def hem(s):#荷尔蒙
    if (s=="1报告统计"):
        in1=input('请问你有喜欢的女生吗？ 1没有 2有')
    else:
        in1=input('请问你有喜欢的男生吗？ 1没有 2有')
    if (s == "1报告统计"):
        in2 = input('请问你短视频刷到小姐姐会点赞吗？ 1不会 2会')
    else:
        in2 = input('请问你短视频刷到小哥哥会点赞吗？ 1不会 2会')
    if (s == "1报告统计"):
        in3 = input('现实生活中你愿意主动与女生讲话吗？ 1不愿意 2愿意')
    else:
        in3 = input('现实生活中你愿意主动与男生讲话吗？ 1不愿意 2愿意')
    if (s == "1报告统计"):
        in4 = input('现实生活中女生犯小错你会很厌烦她吗？ 1不会 2会')
    else:
        in4 = input('现实生活中男生犯小错你会很厌烦她吗？ 1不会 2会')

    df=(int(in1)-1)*5+(int(in2)-1)*5+(int(in3)-1)*5+(2-int(in4))*5
    return df

def sao(s):#聊骚
    if (s == "1报告统计"):
        in1 = input('请问你有用过除qq,微信以外的交友软件吗？ 1没有 2有')
    else:
        in1 = input('请问你有用过除qq,微信以外的交友软件吗？ 1没有 2有')
    if (s == "1报告统计"):
        in2 = input('请问你是否会找女生倾诉你的心事？ 1不会 2会')
    else:
        in2 = input('请问你是否会找男生倾诉你的心事？ 1不会 2会')
    if (s == "1报告统计"):
        in3 = input('你有在网上发过自拍照吗？ 1没有 2有')
    else:
        in3 = input('你有在网上发过自拍照吗？ 1没有 2有')
    if (s == "1报告统计"):
        in4 = input('你有对女生说过土味情话吗？ 1没有 2有')
    else:
        in4 = input('你有对男生说过土味情话吗？ 1没有 2有')

    df = (int(in1) - 1) * 5 + (int(in2) - 1) * 5 + (int(in3) - 1) * 5 + (int(in4)-1) * 5
    return df

def yan(s):#颜装
    if (s == "1报告统计"):
        in1 = input('请问你有过被陌生女生夸好看吗？ 1没有 2有')
    else:
        in1 = input('请问你有过被陌生男生夸好看吗？ 1没有 2有')
    if (s == "1报告统计"):
        in2 = input('在生活中的公共场所有被人偷看的经历？ 1没有 2有')
    else:
        in2 = input('在生活中的公共场所有被人偷看的经历？ 1没有 2有')
    if (s == "1报告统计"):
        in3 = input('在集体中有没有被女生特别关照过？ 1没有 2有')
    else:
        in3 = input('在集体中有没有被男生特别关照过？ 1没有 2有')
    if (s == "1报告统计"):
        in4 = input('你是否经常询问联系方式？ 1没有 2有')
    else:
        in4 = input('你是否经常询问联系方式？ 1没有 2有')

    df = (int(in1) - 1) * 5 + (int(in2) - 1) * 5 + (int(in3) - 1) * 5 + (int(in4)-1) * 5
    return df

def zha(s):#鉴渣
    if (s == "1报告统计"):
        in1 = input('请问你有考虑过追求比你各方面条件差的女生吗？ 1没有 2有')
    else:
        in1 = input('请问你有过刻意贬低男生认为他比你差吗？ 1没有 2有')
    if (s == "1报告统计"):
        in2 = input('在生活中你喜欢过多个女生吗？ 1没有 2有')
    else:
        in2 = input('在生活中你喜欢过多个男生吗？ 1没有 2有')
    if (s == "1报告统计"):
        in3 = input('如果和女生处对象愿意带她见你的家人或是朋友吗？ 1不愿意 2愿意')
    else:
        in3 = input('如果和男生处对象会回报男生的付出吗？ 1基本不会 2会')
    if (s == "1报告统计"):
        in4 = input('你常常有空吗？ 1没有 2有')
    else:
        in4 = input('你会强制他人顺从你的心意吗？ 1不会 2会')

    df = (int(in1) - 1) * 5 + (int(in2) - 1) * 5 + (2-int(in3)) * 5 + (int(in4)-1) * 5
    return df

def yong(s):#勇气
    if (s == "1报告统计"):
        in1 = input('请问你对和喜欢的人的未来抱有自信吗？ 1没有 2有')
    else:
        in1 = input('请问你对和喜欢的人的未来抱有自信吗？ 1没有 2有')
    if (s == "1报告统计"):
        in2 = input('你愿意为自己的对象吃苦吗？ 1不愿意 2愿意')
    else:
        in2 = input('你愿意为自己的对象吃苦吗？ 1不愿意 2愿意')
    if (s == "1报告统计"):
        in3 = input('你敢在喜欢的人面前说出自己的缺点并承诺改错吗？ 1怂 2敢')
    else:
        in3 = input('你敢在喜欢的人面前说出自己的缺点并承诺改错吗？ 1怂 2敢')
    if (s == "1报告统计"):
        in4 = input('你有勇气向喜欢的人告白吗？ 1没有 2有')
    else:
        in4 = input('你有勇气向喜欢的人告白吗？ 1没有 2有')

    df = (int(in1) - 1) * 5 + (int(in2) - 1) * 5 + (int(in3)-1) * 5 + (int(in4)-1) * 5
    return df

a='y'
while a=='y':
    name=input('请输入姓名')
    print(f"\n你好！{name}欢迎参加脱单测试！\n")

    sex=input('请问你的性别是：1男 2女')
    score=hem(sex)+sao(sex)+yan(sex)+zha(sex)+yong(sex)
    print(score)
    #--------评价------------
    if score < 60:
        print('算了吧！单身狗！┑(￣Д ￣)┍')
    elif 60 <= score < 70:
        print('有机会，不多 (ˉ▽￣～) 切~~')
    elif 70<= score < 80:
        print('干巴爹(๑•̀ㅂ•́) ✧')
    elif 80<=score<90:
        print('大大的可能性φ(≧ω≦*)♪')
    else:
        print('速脱ᕕ(◠ڼ◠)ᕗ')
    a=input('是否再玩一次？y/n')
    if a=='y':
        continue
    else:
        break