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


a='y'
#------重玩选项---------
while a=='y':
    #-----进行选择---------
    b=input('玩1.肥胖计算器还是2.绩点计算器？1报告统计/2弹幕')
    if b=='1报告统计':
        height = float(input('请输入你的身高(米）'))
        weight = float(input('请输入你的体重（千克）'))
        IBM = weight / (height ** 2)
        print('你的IBM指数是%.2f'%IBM)
        if IBM < 18:
            print('瘦子')
        elif 18 <= IBM <= 24:
            print('刚刚好')
        elif 24 <= IBM <= 28:
            print('微胖')
        else:
            print('胖')
    else:
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
                   '职业发展规划'}  # ----------------次取出对象

        for subject in classes:
            total_gpa = 0

            # -------限制输入，使符合规定条件-------------
            while True:
                # -------判断是否全为数字----------
                while True:
                    grade = input(f'{name}同学请输入{subject}成绩：')  # ----录入成绩-----
                    try:
                        grade = float(grade)  # -------尝试浮点化------

                        break  # ---------------结束while循环-------
                    except ValueError:  # ------如果失败，重新输入-------
                        print('请重新输入')
                if 0 <= grade <= 100:
                    break
                else:
                    continue

            # -------判断数字的合理性-------------------

            gpa = single_gpa(grade)
            if gpa is not None:
                total_gpa += gpa  # -----------计算绩点和

        # ------------计算平均值-----------------
        average_gpa = total_gpa / 12
        print(f'{name}同学，你的加权绩点是%.2f' % average_gpa)

    a=input('是否再玩一次y/n')