import turtle


def motion(event):
    x, y = event.x, event.y
    print(f"鼠标位置：{x}, {y}")


game = turtle.Screen()
# 窗口大小
width = 800
height = 1000
game.setup(height, width)
canvas = game.getcanvas()
canvas.bind('<Motion>', motion)  # <Motion> 是 Tkinter 中用于表示鼠标移动的事件类型的标准字符串,将鼠标移动事件（<Motion>）与一个名为 motion 的函数绑定在一起
game.mainloop()
