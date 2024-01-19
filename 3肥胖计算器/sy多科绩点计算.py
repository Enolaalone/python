def single_gpa(g):#定义单科绩点
    while True:
        if (g >= 0) and (g < 60):#----------60以下--------
            a = 0
            return a
            break
        elif (g >= 60) and (g < 70):#---------60-70---------
            a = g % 60 * 0.1 + 1
            return a
            break
        elif (g >= 70) and (g < 80):#-----------70-80--------
            a = g % 70 * 0.1 + 2
            return a
            break
        elif (g >= 80) and (g < 90):#---------80-90-----------
            a = g % 80 * 0.1 + 3
            return a
            break
        elif (g >= 90) and (g < 100):#---------90-100----------
            a = g % 90 * 0.1 + 4
            return a
            break
        else:
            print('错误，请重新输入')
            return None

#函数一定要用return返回值
#-----------------------------------------


#------绩点求和实验---------
'''classes={'语文','英语',}
total_gpa=0
for subject in classes:
    grade= float(input(f'请输入你的{subject}的成绩'))
    gpa=single_gpa(grade)

    if gpa is not None:
        total_gpa+=gpa
print(total_gpa)'''

#---------成绩录入备份--------

b='y'
while b=='y':
    name = (input('请输入姓名'))
    classes = {'人文素质教育',
               '大学英语',
               '大学英语听说',
               '体育',
               '形势与政策',
               '中国近代史纲要 ',
               '高等数学B',
               '计算机科学概论',
               '军事技能',
               '军事理论',
               '心理健康教育',
               '职业发展规划'}

for subject in classes:
    total_gpa = 0
    grade = float(input(f'{name}同学请输入{subject}成绩：'))  # ----录入成绩-----

    gpa = single_gpa(grade)
    if gpa is not None:
        total_gpa += gpa


end_gpa = total_gpa / 11
print(f'{name}同学，你的加权绩点是%.2f' % end_gpa)
b = input('是否要再试一试，y/n')

'''1报告统计---------f 字符串前缀（formatted string literals）是Python3.6版本引入的一项特性，
它允许你在字符串中插入变量，而不需要使用 + 连接符或者 str() 函数将变量转换为字符串。
在一个带有 f 前缀的字符串中，你可以使用大括号 {} 来包含变量或表达式，这个变量或表达式将会在字符串被格式化时被替代。'''