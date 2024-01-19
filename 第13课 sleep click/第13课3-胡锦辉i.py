# -----初始化---------------------
import turtle as t
import random

t.bgcolor('pink')

A = ['\u264B', '\u2648', '\u2649', '\u264F', '\u264E', '\u264A', '\u264D', '\u2653', '\u264C', '\u2652', '\u2650']
B = []  # 随机生成列表元素
C = []
k = 'y'
g = 0


def p(x, y):  # onscreenclick内置函数，（x,y)必须有测定坐标值
    move(-500, 80)
    t.write(B[8], align='center', font=('宋体', 120, 'normal'))  # 显示结果


def q(x, y):
    global g
    g = 1


def move(x, y):  # 移动函数
    t.hideturtle()
    t.up()
    t.goto(x, y)
    t.down()


def write1(x, y, i, size):  # 写字函数
    move(x, y)
    t.color('black')
    t.write(i, align='center', font=('宋体', size, 'normal'))


def shuijin(x, y, r):  # 画水晶球
    move(x, y - r)
    t.color('skyblue')
    t.begin_fill()
    t.circle(r)
    t.end_fill()


b = random.randint(0, len(A) - 1)
for i in range(100):
    if (i + 1) % 9 == 0:  # -------保证9的倍数一样
        B.append(A[b])
    else:
        a = random.randint(0, len(A) - 1)
        B.append(A[a])

t.tracer(False)  # 快速显示
shuijin(-500, 100, 200)
write1(-500, 360, '吉普赛读心术', '90')
write1(-500, -250, '  这是一个吉普赛人古老的神秘读心术，它能测算\n'
                   '出，你内心的感应，屡试不爽，非常可怕。\n  在心中'
                   '10~99之间任意挑选一个数，用这个数\n先减去它十位上的数'
                   '，再减去个位上的数，得到\n最终数。在图表中找出最终数对应的图形'
                   '并把这\n个图形牢记在心中。然后点击水晶球，它将会看穿\n你的内心！！！\n'
                   '  例如：你选的是25，25-2弹幕-5=最终数'
       , '12')  # ----------------------文字部分

# --------------------for in 双循环绘制列表
t.up()
for j in range(10):
    move(-120, 200 - 50 * j)
    for i in range(10):
        t.write(f'{j * 10 + i + 1}{B[j * 10 + i]}', align='center', font=('宋体', 35, 'normal'))
        t.fd(100)
move(-168, -300 + 50)
t.down()
# ---------------------------------------
for i in range(12):
    t.fd(1000)
    move(-170, -300 + 50 + 50 * i)

t.left(90)

for i in range(12):
    move(-170 + 100 * i, -300 + 50)
    t.fd(500)
t.up()
# ---------------以上绘制表格
t.tracer(True)
t.onscreenclick(p)
t.done()
