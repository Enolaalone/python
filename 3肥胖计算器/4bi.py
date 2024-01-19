def flag_4(w,x,y):
    import math
    import turtle as t
    t.speed(0)

    # -------移动笔头---------
    def move(x, y):  # 高速移动画笔
        t.speed(0)
        t.hideturtle()  # 隐藏画笔
        t.pensize(0.2)  # 定义笔大小
        t.penup()
        t.goto(x, y)
        t.pendown()

    def wuxing_flag(w, x, y):#---画五星红旗------

        def hongbu(w,x,y):#------红布
            move(x, y)
            t.seth(0)
            t.color('red')
            t.begin_fill()
            for i in range(2):
                t.forward((3 / 2) * w)
                t.left(90)
                t.forward(w)
                t.left(90)
            t.end_fill()

        hongbu(w, x, y)


        # ---画小星星--------
        def little_star(w, a, b, x, y):  # --w旗宽--a/b---tan值----(X,Y)-----右上两颗星星
            l_s = 2 * w / 20 * math.cos(math.pi / 10)
            d1 = 18 + 180 / math.pi * math.atan(a / b)
            dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
            x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
            y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

            move(w / 4 + x + x1, w * 3 / 4 + y + y1)  # 移动到位

            t.setheading(d1)
            t.fillcolor("yellow")
            t.begin_fill()
            for i in range(5):
                t.forward(l_s)
                t.right(144)
            t.end_fill()

        def alittle_star(w, a, b, x, y):  # ---右下两颗星星
            l_s = 2 * w / 20 * math.cos(math.pi / 10)
            d1 = 18 - 180 / math.pi * math.atan(a / b)
            dtc = math.sqrt((a * w / 20) ** 2 + (b * w / 20) ** 2)
            x1 = (dtc - l_s / 2) * math.cos(math.atan(a / b))
            y1 = (dtc - l_s / 2) * math.sin(math.atan(a / b))

            move(w / 4 + x + x1, w * 3 / 4 + y - y1)

            t.setheading(d1)
            t.fillcolor("yellow")
            t.begin_fill()
            for i in range(5):
                t.forward(l_s)
                t.right(144)
            t.end_fill()

        # ----------画大星星--------
        def b_star(w,x,y):
            move(w / 4 + x, y + 9 / 10 * w)
            l_b = 6 * w / 20 * (math.cos(math.pi / 10))
            t.setheading(-72)
            t.pencolor('yellow')  # 修改笔颜色
            t.fillcolor("yellow")
            t.begin_fill()
            for i in range(5):
                t.forward(l_b)
                t.right(144)
            t.end_fill()

        b_star(w, x, y)

        # -------小星星们-------上/下
        little_star(w, 3, 5, x, y)
        little_star(w, 1, 7, x, y)

        alittle_star(w, 2, 7, x, y)
        alittle_star(w, 4, 5, x, y)


#------公用一个模块-------
    wuxing_flag(w,x,y)
    wuxing_flag(w,x-3/2*w-10,y)
    wuxing_flag(w,x-3/2*w-10,y-w-10)
    wuxing_flag(w,x,y-w-10)
    t.done()

flag_4(400,0,0)