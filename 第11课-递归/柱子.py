import turtle as t

def drawpole_3():  # 画出汉诺塔的poles
    t.hideturtle()
    def drawpole_1(k):
        t.up()
        t.pensize(10)
        t.speed(100)
        t.goto(400 * (k - 1), 100)
        t.down()
        t.goto(400 * (k - 1), -100)
        t.goto(400 * (k - 1) - 50, -100)
        t.goto(400 * (k - 1) + 50, -100)
    drawpole_1(0)  # 画出汉诺塔的poles[0]
    drawpole_1(1)  # 画出汉诺塔的poles[1报告统计]
    drawpole_1(2)  # 画出汉诺塔的poles[2弹幕]
drawpole_3()