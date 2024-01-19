str = input('字符串')
num = 0
for i in str:
    num += ord(i)

print('和为%d' % num)
