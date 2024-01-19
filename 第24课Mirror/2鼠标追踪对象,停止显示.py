import turtle


class Mouse(turtle.Turtle):
    def __init__(self):
        super().__init__()  # 继承turtle
        self.hideturtle()
        self.move = False  # 显示移动状态

    def circle_l(self, event):
        x, y = event.x - width / 2, event.y - height / 2  # 转换坐标系
        # print(x, y)  # 打印位置
        r = 20

        id_1 = canvas.create_oval(x - r, y + r, x + r, y - r, fill='black')
        id_2 = canvas.create_oval(-x - r, y + r, -x + r, y - r, fill='black')
        canvas.after(20, lambda: canvas.delete(id_1, id_2))


game = turtle.Screen()
# 窗口大小
width = 1000
height = 800
game.setup(width, height)
canvas = game.getcanvas()

mouse = Mouse()
canvas.bind('<Motion>', mouse.circle_l)

mouse = Mouse()
turtle.done()
game.mainloop()
