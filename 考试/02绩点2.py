grade=float(input("输入成绩"))
if grade<60:
    grade_point=0
    print("你的绩点是%.1f"%grade_point)
else:
    grade_point=(grade-50)/10
    print("你的绩点是%.1f" % grade_point)
