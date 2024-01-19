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

    def drop(self):  # 雨滴
        turtle.tracer(0)
        self.color(self.colors)
        self.begin_fill()
        for _ in range(2):
            self.fd(self.wide1)
            self.circle(5, 90)  # 小园弧
            self.fd(self.long1)
            self.circle(5, 90)  # 小园弧
        self.end_fill()
        turtle.tracer(1)

    def pen_move(self, x, y):
        # 画笔移动
        self.pu()
        self.goto(x, y)
        self.pd()

    def drop_move(self):
        self.pen_move(self.x, self.y)  # 到达顶端
        speed1 = 0  # 初始速度
        # 下落效果
        while 1:
            # print(111)
            turtle.tracer(100)
            speed1 += self.speeds
            self.clear()
            time.sleep(0.2)
            self.pen_move(self.x, self.y-speed1)  # 向下移动
            self.drop()
            if self.ycor() <= (-height / 2 - 2 * self.long1):
                speed1=0


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
# -----------------------------

drop1 = Drop('black', 30, 0, height/2)
drop1.drop_move()
turtle.done()
game.mainloop()
