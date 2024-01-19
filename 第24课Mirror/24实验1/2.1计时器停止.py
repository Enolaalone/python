import time
import turtle


class TimeCheck(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()  # 继承turtle
        self.width = 100
        self.height = 50
        self.x = x
        self.y = y
        self.hideturtle()  # 隐藏画笔
        # 写字笔的初始化
        self.a = turtle.Pen()  # 注册画笔
        self.a.hideturtle()
        self.a.right(90)  # 从左往右写
        self.a.up()
        self.a.goto(self.x + self.height, self.y - self.width * (5 / 12))
        self.a.color('red')
        # 时间部分
        self.second = 0  # 设置秒表起始量
        self.time_status = True

    def cell(self):  # 绘制计时器的框
        turtle.tracer(0)
        self.pu()
        self.goto(self.x, self.y)
        self.pd()

        self.color('lightgrey')  # 底色
        self.begin_fill()
        for _ in range(2):
            self.fd(self.width)
            self.right(90)
            self.fd(self.height)
            self.right(90)
        self.end_fill()
        turtle.tracer(1)

    def time_1(self):  # 计时器部分
        turtle.tracer(100)
        if self.time_status:
            self.a.clear()
            self.second += 1
            self.a.write(self.second, align='center', font=('宋体', 30, 'normal'))  # 写时间
        turtle.ontimer(self.time_1, 1000)  # 1秒后自我调用

    def start(self):
        self.cell()
        self.time_1()

    def stop(self, event):  # BInd函数调用必须包含event
        self.time_status = False
        print(123)


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
canvas = game.getcanvas()
# 计时器模板
timecheck = TimeCheck(-width / 2, height / 2)
timecheck.start()

canvas.bind('<Button-1>', timecheck.stop)  # 将<Motion>鼠标移动事件和，时间停止函数联系

turtle.done()
game.mainloop()
