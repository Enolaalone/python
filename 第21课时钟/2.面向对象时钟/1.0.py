import datetime as dt
import turtle as t

class Clock:
    def __init__(self,r=200):
        self.turtle=t
        self.r=r
        self.a = t.Pen() # 秒
        self.b = t.Pen()  # 分钟
        self.c = t.Pen()  # 小时
        self.window = t.Screen()  # 设定屏幕
        self.wheel(200)
        self.sec = self.pointer(90, '秒针', 10, self.a, 'black')
        self.minute = self.pointer(70, '分针', 10, self.b, 'blue')
        self.hour = self.pointer(40, '时针', 10, self.c, 'red')
        self.tm = dt.datetime.today()
        self.s = self.tm.second  # 秒
        self.m = self.tm.minute  # 分
        self.h = self.tm.hour  # 小时
        self.renew()  # 死循环自己调用自己
        self.window.mainloop()  # 使屏幕持续存在

    def pointer(self,length, name, width, a, color):  # 画指针
        t.reset()  # 每执行一次，从新设置
        t.hideturtle()
        t.pu()
        t.begin_poly()  # 记录图形
        t.fd(length)  # 从0开始
        t.end_poly()
        t.register_shape(name, t.get_poly())  # 注册记录的图形
        # a.hideturtle()
        a.pencolor(color)
        a.shape(name)
        a.shapesize(2, 1, width)

        return a  # 画笔a作为对象返回

    # ---------------------------------------------

    def renew(self):
        global s
        global m
        global h
        t.tracer(0)
        t.clear()
        tm = dt.datetime.today()  # 返回当下时间
        # print(tm)
        # --------------------联动效果

        if self.s == 60:  # 满一分钟
            self.s = 0
            self.m += 1
        if self.m == 60:  # 满一小时
            self.m = 0
            self.h += 1
        if self.h == 24:
            self.h = 0
        t.pu()
        t.goto(-6, 0)
        t.pd()
        t.write(f'{tm:%Y-%m-%d %H:%M:%S}', align='center', font=('Courier', 14, 'bold'))  # Courier计算机字体
        self.sec.seth(180 - 6 * self.s)  # 秒钟，起始为12
        self.minute.seth(180 - 6 * self.m - 6 * (self.s / 60))  # 分钟，起始为12
        self.hour.seth(180 - 30 * self.h - 30 * (self.m / 60))
        t.tracer(1)
        self.s += 1  # 加一秒
        t.ontimer(self.renew, 1000)  # 1s执行程序一次

    # ----------------------------------------------------------------------------------------------------------------------
    # ============================画表盘
    def wheel(self,r):  # r半径
        b = t.Pen()
        b.hideturtle()
        b.pu()
        x, y = b.position()
        b.goto(x, y - r)
        b.pd()
        b.width(10)
        # b.seth(180)
        t.tracer(0)
        A = [6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4, 5]  # 画表盘
        for i in A:  # 数字部分
            b.write(i, align='center', font=('Courier', 30, 'bold'))
            b.dot(10)
            b.up()
            b.circle(r, -30)
            b.pd()

        for i in range(60):  # 小格子
            b.dot(6)
            b.up()
            b.circle(r, -6)
            b.pd()
        t.tracer(1)
        t.seth(0)


if __name__ == "__main__":
    clock = Clock()