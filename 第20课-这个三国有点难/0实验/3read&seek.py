with open('小超市商品.txt','r') as f:#必须使用rb

    a=f.read(6)#文本解读read,后加字符串个数
    print(a)