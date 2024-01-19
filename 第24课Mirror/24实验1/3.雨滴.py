import time
import turtle


class Drop(turtle.Turtle):  # 雨滴
    def __init__(self, colors, speeds, x, y):
        super().__init__()  # 继承
        self.hideturtle()  # 隐藏笔头
        self.colors = colors  # 颜色
        self.speeds = speeds  # 速度
        self.wide1 = 10  # 宽
        self.long1 = 30  # 长
        self.r1 = 5  # 弧半径
        self.x = x  # 位置
        self.y = y

    def drop(self):
        turtle.tracer(0)
        self.color(self.colors)
        self.begin_fill()
        for _ in range(2):
            self.fd(self.wide1)
            self.circle(5, 90)  # 小园弧
            self.fd(self.long1)
            self.circle(5, 90)
        self.end_fill()
        turtle.tracer(1)




game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
# -----------------------------

drop1 = Drop('black', 10, 0, 0).drop()

turtle.done()
game.mainloop()
