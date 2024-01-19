def single_gpa(g):# ----------定义单科绩点
    if (g >= 0) and (g < 60):  # ----------60以下--------
        a = 0
        return a
    elif (g >= 60) and (g < 70):  # ---------60-70---------
        a = g % 60 * 0.1 + 1
        return a
    elif (g >= 70) and (g < 80):  # -----------70-80--------
        a = g % 70 * 0.1 + 2
        return a
    elif (g >= 80) and (g < 90):  # ---------80-90-----------
        a = g % 80 * 0.1 + 3
        return a
    elif (g >= 90) and (g < 100):  # ---------90-100----------
        a = g % 90 * 0.1 + 4
        return a
    else:
        print('错误，请重新输入')
        return None

#-------开始计算--------
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
               '职业发展规划'}#----------------次取出对象

    for subject in classes:
        total_gpa = 0

#-------限制输入，使符合规定条件-------------
        while True:
            # -------判断是否全为数字----------
            while True:
                grade = input(f'{name}同学请输入{subject}成绩：')  # ----录入成绩-----
                try:
                    grade=float(grade)#-------尝试浮点化------

                    break#---------------结束while循环-------
                except ValueError:#------如果失败，重新输入-------
                    print('请重新输入')
            if 0<=grade<=100:
                break
            else:
                 continue


 #-------判断数字的合理性-------------------

        gpa = single_gpa(grade)
        if gpa is not None:
             total_gpa += gpa#-----------计算绩点和



#------------计算平均值-----------------
    average_gpa = total_gpa / 11
    print(f'{name}同学，你的加权绩点是%.2f' %average_gpa)

    b = input('是否要再试一试，y/n')





