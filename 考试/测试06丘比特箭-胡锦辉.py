import turtle as t
import time
def draw_arrow():
    # 创建画布和箭头
    screen = t.Screen()
    t.shape("classic")# 设置箭头形状
    t.color("pink")
    t.shapesize(2, 2)   #设置箭头大小

    while True:  # 屏幕右侧的 x 坐标
        t.pd()
        t.forward(80)  # 控制箭头移动的速度
        t.tracer(0)
        t.clear()# 清除箭头轨迹
        time.sleep(0.05)
        t.tracer(1)
        if t.xcor()>400:
            t.tracer(0)
            t.pu()
            t.goto(-400,0)
            t.tracer(1)

draw_arrow()