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


a=single_gpa(96)
print(a)