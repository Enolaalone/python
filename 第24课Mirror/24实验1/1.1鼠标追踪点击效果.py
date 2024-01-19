import turtle


def motion(event):  # 移动事件
    x, y = event.x, event.y-height/2
    # print(f"鼠标位置：{x}, {y}")



def click_1(event):  # 点击打印位置
    x, y = event.x, event.y
    print(x, y)#打印位置


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
canvas = game.getcanvas()
canvas.bind('<Motion>', motion)  # 将<Motion>鼠标移动事件和，motion 函数联系
canvas.bind('<Button-1>', click_1)  # 将<Button-1>鼠标左键点击事件事件和，click函数联系

game.mainloop()
