import turtle
from typing import Any


def click_1(event):  # 点击打印位置
    x, y = event.x - width / 2, event.y - height / 2
    print(x, y)  # 打印位置
    print(event.x, event.y)
    r = 20
    id = canvas.create_oval(x - r, y + r, x + r, y - r, fill='black')
    canvas.after(20, lambda: canvas.delete(id))


def move(x, y):
    print(f'turtle{x, y}')


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
canvas = game.getcanvas()
canvas.bind('<Motion>', click_1)  # 将<Motion>鼠标移动事件和，motion 函数联系
# canvas.bind('<Button-1>', click_1)  # 将<Button-1>鼠标左键点击事件事件和，click函数联系
game.mainloop()
