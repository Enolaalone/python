import random as r#简化random
pk=['红心A','红心2','红心3','红心4','红心5','红心6','红心7','红心8','红心9','红心10','红心J','红心Q','红心K', \
    '梅花A','梅花2','梅花3','梅花4','梅花5','梅花6','梅花7','梅花8','梅花9','梅花10','梅花J','梅花Q','梅花K', \
    '方块A','方块2','方块3','方块4','方块5','方块6','方块7','方块8','方块9','方块10','方块J','方块Q','方块K', \
    '黑桃A','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K', \
    'joker','JOKER']#牌库
def fa():
    nm1=[]#农民1
    nm2=[]#农民1
    dizhu=[]#地主
    for i in range(0,54,3):
        a=r.randint(0,53-i)#抽一个数集合就少一个元素-i
        nm1.append(pk[a])
        del pk[a]#删除pk[]中的a号元素
        a = r.randint(0, 52- i)
        nm2.append(pk[a])
        del pk[a]
        a = r.randint(0, 51- i)
        dizhu.append(pk[a])
        del pk[a]
    #分别从农民抽两牌给地主17-17-20
    a=r.randint(0,16)
    dizhu.append(nm1[a])
    del nm1[a]
    a = r.randint(0, 16)
    dizhu.append(nm2[a])
    del nm2[a]
    #显示牌
    print(f'农民1的牌:{nm1}')
    print(f'农民2的牌:{nm2}')
    print(f'地主的牌:{dizhu}')

fa()

