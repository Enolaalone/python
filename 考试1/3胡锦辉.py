
while(1):
    grade = int(input('成绩'))
    if grade<60:
        print('不及格')
    elif 60<=grade<=69:
        print('及格')
    elif 70<=grade<=79:
        print('一般')
    elif 80<=grade<=89:
        print('良好')
    elif 90<=grade<=99:
        print('优秀')
    elif grade==100:
        print('满分')
    else:
        print('输入有误')