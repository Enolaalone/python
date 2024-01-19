import turtle as t
def creat_plates(n):  # 制造n个盘子
    plates = [t.Turtle() for i in range(n)]
    for i in range(n):
        plates[i].up()
        plates[i].hideturtle()
        plates[i].shape("square")
        plates[i].shapesize(1, 8 - i)
        plates[i].goto(-400, -90 + 20 * i)
        plates[i].showturtle()
    return plates
creat_plates(5)