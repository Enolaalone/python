import random
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
        self.speed1 = 0  # 初始速度

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
        # 下落效果
        turtle.tracer(100)
        self.speed1 += self.speeds
        self.clear()
        self.pen_move(self.x, self.y-self.speed1)  # 向下移动
        self.drop()
        if self.ycor() <= (-height / 2-2*self.long1 ):
            self.speed1=0
            self.pen_move(random.randint(-350,0), self.y)
        turtle.ontimer(self.drop_move,1000)


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
# -----------------------------
drops = [Drop('black',random.randint(50,200), i * 70 - width / 2, height / 2) for i in range(6)]#创建10雨滴
for drop in drops:
    drop.drop_move()

turtle.done()
game.mainloop()
