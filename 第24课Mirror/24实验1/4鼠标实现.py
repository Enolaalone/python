import random
import threading
import time
import turtle


class Drop(turtle.Turtle):  # 雨滴
    def __init__(self, colors, x, y, left, right):
        super().__init__()  # 继承
        self.colors = colors  # 颜色
        self.long1 = 45  # 长
        self.x = x  # 位置
        self.y = y
        self.shape('circle')
        # self.hideturtle()  # 隐藏笔头
        self.shapesize(1)  # 设置笔的宽度
        self.seth(-90)
        self.color(self.colors)
        # ----生成范围
        self.right1 = right
        self.left1 = left
        #-----速度改
        self.speeds=random.randint(1,10)
        self.pen_move(self.x,self.y)


    def drop(self):  # 雨滴
        turtle.tracer(0)
        self.fd(self.long1)
        turtle.tracer(1)

    def pen_move(self, x, y):
        # 画笔移动
        self.pu()
        self.goto(x, y)
        # self.pd()

    def drop_move(self):
        # turtle.tracer(50)
        # 下落效果
        # self.clear()
        # self.drop()
        self.pen_move(self.x,-height / 2- 2 * self.long1)
        if self.ycor() <= (-height / 2 ):#如果出界
            self.x = random.randint(self.left1, self.right1)
            self.pen_move(self.x, self.y)
        turtle.ontimer(self.drop_move, 1000)


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
# -----------------------------
drops_l = [Drop('black', (i + 1) * 70 - width / 2, height / 2,-380,-50) for i in range(4)]  # 创建6雨滴
drops_r = [Drop('red', -(i + 1) * 70 + width / 2, height / 2,50,300) for i in range(4)]  # 创建6雨滴
for i in drops_r:#合并
    drops_l.append(i)
for drop in drops_l:
    threading.Thread(target=drop.drop_move(),).start()


game.mainloop()
