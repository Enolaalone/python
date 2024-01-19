import turtle

# 参数设置
DISK_HEIGHT = 30
DISK_WIDTH = 150
DISTANCE_BETWEEN_PEGS = 250

# 设置turtle
wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
t.speed(0)  # 最快速度

def draw_peg(x, y):
    t.penup()
    t.goto(x, y - 150)
    t.pendown()
    t.goto(x, y + 150)

def move_disk(source, target):
    disk = source.pop()
    y = -150 + len(target) * DISK_HEIGHT
    x_target = -DISTANCE_BETWEEN_PEGS + target.index([]) * DISTANCE_BETWEEN_PEGS
    t.penup()
    t.goto(disk.xcor(), y)
    target.append(disk)

def hanoi(n, source, target, auxiliary):
    if n == 0:
        return
    hanoi(n-1, source, auxiliary, target)
    move_disk(source, target)
    wn.update()  # 更新画面
    hanoi(n-1, auxiliary, target, source)

# 初始化三个柱子
pegs = [[], [], []]
for i in range(3):
    draw_peg(-DISTANCE_BETWEEN_PEGS + i * DISTANCE_BETWEEN_PEGS, 0)

# 创建盘子并放置在第一个柱子上
colors = ["red", "green", "blue"]
for i in range(3):
    disk = turtle.Turtle()
    disk.shape("square")
    disk.shapesize(1, (3-i)/2)  # 调整大小
    disk.color(colors[i])
    disk.penup()
    disk.goto(-DISTANCE_BETWEEN_PEGS, -150 + i * DISK_HEIGHT)
    pegs[0].append(disk)

# 执行汉诺塔算法
wn.tracer(0, 0)  # 关闭自动更新，提高效率
hanoi(len(pegs[0]), pegs[0], pegs[2], pegs[1])
wn.mainloop()