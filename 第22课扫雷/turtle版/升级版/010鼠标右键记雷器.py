import time
import turtle as t
import random as r
import time as tm
import threading


class Mine:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.number = 0  # 周围雷数
        self.status = False  # 是否揭开
        self.is_mine = False  # 是否是雷
        self.click = False  # 点击对象
        self.click_r = False  # 右键检测
        self.mine_size = 40  # 雷大小

    def cell(self, color):  # 画雷的格子
        t.color(color)
        t.begin_fill()
        for i in range(4):
            t.fd(self.mine_size)
            t.left(90)
        t.end_fill()
        t.color('white')
        for i in range(4):
            t.fd(self.mine_size)
            t.left(90)
        t.end_fill()

    def reveal(self):  # 雷的各种状态改变
        t.tracer(0)
        if self.status == False:  # 未被揭开状态----------------------调试改为True
            if not self.click_r:
                t.hideturtle()
                t.up()
                t.goto(self.x - self.mine_size / 2, self.y - self.mine_size / 2)
                t.pd()
                self.cell('grey')  # 内部函数调用
                t.tracer(1)
            else:  # 右键点击增加红旗
                t.up()  #
                t.goto(self.x, self.y - self.mine_size / 2 + 1)  #
                t.pd()  #
                t.color('black')  #
                t.goto(self.x, self.y + self.mine_size / 2 - 1)  #
                t.right(30)  #
                t.color('red')  #
                t.begin_fill()  #
                for _ in range(3):  #
                    t.fd(self.mine_size / 2)  #
                    t.right(120)  #
                t.end_fill()  #
                # 复原
                t.color('black')
                t.left(30)


        else:  # 揭开状态下
            if self.is_mine == True:  # 是雷
                if self.click == False:
                    # ------------
                    t.pu()
                    t.goto(self.x - 20, self.y - 20)
                    t.pd()
                    self.cell('lightgrey')
                    # -----------------画雷
                    t.hideturtle()
                    t.pu()
                    t.goto(self.x, self.y - 10)
                    t.pd()
                    t.color('black')
                    t.begin_fill()
                    t.circle(self.mine_size / 4)
                    t.end_fill()
                    # -------------
                    t.tracer(1)
                else:
                    # ------------
                    t.pu()
                    t.goto(self.x - 20, self.y - 20)
                    t.pd()
                    self.cell('red')
                    # -----------------画雷
                    t.hideturtle()
                    t.pu()
                    t.goto(self.x, self.y - 10)
                    t.pd()
                    t.color('black')
                    t.begin_fill()
                    t.circle(self.mine_size / 4)
                    t.end_fill()
                    # -------------
                    t.tracer(1)

            else:
                if self.number > 0:  # 周围有雷
                    # -------------------------
                    t.pu()
                    t.goto(self.x - 20, self.y - 20)
                    t.pd()
                    self.cell('lightgrey')
                    # 写数字
                    t.hideturtle()
                    t.pu()
                    t.goto(self.x, self.y - 10)
                    t.pd()
                    # -------区别颜色-------------
                    if self.number == 1:
                        t.color('blue')
                    if self.number == 2:
                        t.color('green')
                    if self.number >= 3:
                        t.color('red')

                    t.write(self.number, align='center', font=('宋体', 17, 'bold'))

                    t.tracer(1)
                else:  # 周围雷是0
                    t.hideturtle()
                    t.up()
                    t.goto(self.x - 20, self.y - 20)
                    t.pd()
                    self.cell('lightgrey')
                    t.tracer(1)


class Mineboard:
    def __init__(self):
        # t.hideturtle()
        # ------注册形状-----------------
        t.register_shape('cool.gif')
        t.register_shape('smile.gif')
        t.register_shape('dead.gif')

        # -----------------------------------------
        '''mine=Mine(0,0)#创建具体的对象才可继续调用内部函数
        mine.reveal()'''

        self.time_status = True  # 计时状态

        # -------------游戏初始化------------------------
        self.width = 400
        self.height = 500
        self.row = 10
        self.col = 10
        self.mine_size = 40  # 雷大小
        # ----------游戏初始化-----------------
        self.game = t.Screen()  # 导入屏幕
        self.game.title('扫雷')  # 取名
        self.game.bgcolor('white')  # 设置背景颜色
        self.game.setup(self.width + 10, self.height)  # 游戏窗口大小

        self.start()

    def cell2(self, x, y):  # 计时黑框
        t.tracer(0)
        t.pu()
        t.goto(x, y)
        t.pd()
        t.color('grey')
        t.begin_fill()
        for i in range(2):
            t.fd(4 * self.mine_size)
            t.right(90)
            t.fd(2 * self.mine_size)
            t.right(90)
        t.end_fill()
        t.tracer(1)

    def writer(self, a, x, y, content, size):  # 写数字
        t.tracer(0)
        a.hideturtle()
        a.seth(-90)  # 写字方向
        a.pu()
        a.goto(x, y)
        a.pd()
        a.color('red')
        a.write(content, align='center', font=('宋体', size, 'bold'))
        a.color('black')
        a.seth(0)
        t.tracer(1)

    def emoji(self, a, shape):  # 画表情
        t.tracer(0)
        a.shape(shape)  # 笑脸
        a.shapesize(10, 10)
        a.pu()
        a.goto(0, self.height / 2 - 50)
        t.tracer(1)

    # -------------------触碰反馈---------------
    def on_click(self, x, y):  # 触碰反馈函数
        # print(x,y)#--------检测坐标

        if self.game_status:  # 开始游戏
            if -self.mine_size < x < self.mine_size and 4 * self.mine_size < y < 7 * self.mine_size:  # 重启区域
                # print('yes')
                self.time_status = False  # 开始计时
                # self.d1.clear()

                self.game_status = False  # 游戏结束
                self.restart()
                self.start()

            for i in range(self.row):
                for j in range(self.col):
                    if self.mines[i][j].x - self.mine_size / 2 < x < self.mines[i][j].x + self.mine_size / 2 and \
                            self.mines[i][j].y - self.mine_size / 2 < y < self.mines[i][
                        j].y + self.mine_size / 2:  # 在某个框的范围内
                        if self.mines[i][j].click_r:  # 右键检测
                            self.mines[i][j].click_r = False
                            self.mines[i][j].reveal()
                            self.click_times += 1  # 增加一次插旗机会
                            self.mines_times()

                            break  # 结束循环

                        if self.mines[i][j].is_mine:  # 是雷就结束
                            self.a1.hideturtle()
                            self.b1.showturtle()
                            self.time_status = False  # 计时结束
                            # self.t1.join()#结束进程
                            self.mines[i][j].click = True
                            for k in range(self.row):
                                for l in range(self.col):
                                    if self.mines[k][l].is_mine:
                                        self.mines[k][l].status = True
                                        self.mines[k][l].reveal()
                            self.game_status = False  # 游戏结束

                            # self.game.onclick(None)#停止监听
                        # mines[i][j].status=True
                        # mines[i][j].reveal()#更新cell状态

                        else:
                            self.expend(i, j)  # 如果不是雷就扩展
                            # -----检测是否要结束
                            num = 0
                            for i in range(self.row):
                                for j in range(self.col):
                                    if self.mines[i][j].status:
                                        num += 1
                            if num == 90:
                                self.a1.hideturtle()
                                self.c1.showturtle()
                                self.time_status = False  # 计时结束
                                for k in range(self.row):
                                    for l in range(self.col):
                                        if self.mines[k][l].is_mine:
                                            if not self.mines[k][l].click_r:
                                                self.mines[k][l].click_r = True
                                                self.click_times -= 1
                                                self.mines[k][l].reveal()
                                # self.t1.join()
                                self.game_status = False  # 停止监听

        else:
            if -self.mine_size < x < self.mine_size and 4 * self.mine_size < y < 7 * self.mine_size:  # 重启区域
                # print('yes')
                # self.game_status=False#再次开始
                # self.time_status=True
                self.restart()
                self.start()

    def on_click_r(self, x, y):  # 右键检测
        # print('134')

        for i in range(self.row):
            for j in range(self.col):
                if self.mines[i][j].x - self.mine_size / 2 < x < self.mines[i][j].x + self.mine_size / 2 and \
                        self.mines[i][j].y - self.mine_size / 2 < y < self.mines[i][j].y + self.mine_size / 2 \
                        and self.click_times > 0 and self.mines[i][j].status == False and self.mines[i][
                    j].click_r == False:  # 在某个框的范围内,而且不超过10次
                    self.mines[i][j].click_r = True
                    self.mines[i][j].reveal()
                    self.click_times -= 1
                    self.mines_times()

    # ---------------------递归扩展-------
    def expend(self, i, j):
        if i < 0 or i >= 10 or j < 0 or j >= 10:  # 如果越界就停止
            return

        if self.mines[i][j].status or self.mines[i][j].is_mine or self.mines[i][j].click_r:  # 如果是雷或被揭开就停止
            return

        # if self.mines[i][j].click_r:
        #     self.mines[i][j].click_r=False
        #     self.click_times += 1#
        #     self.mines_times()
        self.mines[i][j].status = True
        self.mines[i][j].reveal()  # 更新cell状态
        if self.mines[i][j].number > 0:  # 边界停止扩展
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:  # 不是本身
                    self.expend(i + dx, j + dy)

    def mines_times(self):  # 标记红旗次数
        self.e1.clear()
        self.cell2(-self.width / 2, 6 * self.mine_size + 1)
        self.e1.color('red')
        self.writer(self.e1, -self.width / 2 + 2 * self.mine_size, self.height / 2 - 2 * self.mine_size,
                    f'{self.click_times}', 50)

    def time_k(self):
        self.cell2(self.width / 2 - 4 * self.mine_size, 6 * self.mine_size + 1)
        time1 = tm.time()
        while self.time_status:
            t.tracer(100)
            tm.sleep(0.2)
            self.d1.clear()
            # t.update()

            time2 = tm.time()
            now = time2 - time1
            self.writer(self.d1, self.width / 2 - 4 * self.mine_size + 2 * self.mine_size,
                        self.height / 2 - 2 * self.mine_size, f'{now:.0f}s', 50)
        # self.writer(self.d1, self.width / 2 - 4 * self.mine_size + 2 * self.mine_size, self.height / 2 - 2 * self.mine_size,f'{now:.0f}s', 50)

    def Tstart(self):
        # 创建一个新线程
        self.t1 = threading.Thread(target=self.time_k())
        self.t1.start()

    def restart(self):  # 再次开始
        self.game.clear()

    def start(self):  # 开始游戏
        t.tracer(0)
        self.a1 = t.Pen()
        self.b1 = t.Pen()
        self.c1 = t.Pen()
        self.d1 = t.Pen()
        self.e1 = t.Pen()
        # -------------表情包管理------------
        self.emoji(self.a1, 'smile.gif')  # 笑
        self.emoji(self.b1, 'dead.gif')  # 死
        self.emoji(self.c1, 'cool.gif')  # 赢
        # 设置笑脸
        self.c1.hideturtle()
        self.b1.hideturtle()
        self.d1.hideturtle()
        self.game_status = True  # 开始游戏
        self.time_status = True
        self.click_times = 10  # 右键点击次数

        self.mines_times()
        # self.t1 = threading.Thread(target=self.time_k, )#时间线程
        # ----------------------------
        # 初始化雷阵列
        self.mines = [[0 for _ in range(self.col)] for _ in range(self.row)]  # 初始化雷阵

        for i in range(self.row):
            for j in range(self.col):
                x = (self.mine_size - self.width) / 2 + j * self.mine_size  # x坐标
                y = (-self.mine_size + self.width) / 2 - i * self.mine_size - (
                            self.height - self.width) / 2 + 10  # y坐标(height-width)/2+10保证接触底线
                self.mines[i][j] = Mine(x, y)
        # ------------------放置地雷-----------------
        # print(mines)
        n = 1
        while n <= 10:
            a, b = r.randint(0, 9), r.randint(0, 9)
            if self.mines[a][b].is_mine == False:
                print(a, b)  # 反馈坐标
                self.mines[a][b].is_mine = True
                # ------------周围雷数加1
                for i in range(a - 1, a + 2):
                    for j in range(b - 1, b + 2):
                        if 0 <= i <= 9 and 0 <= j <= 9:  # 保证在范围内
                            self.mines[i][j].number += 1
                n += 1

        for i in range(self.row):
            for j in range(self.col):
                self.mines[i][j].reveal()

        t.tracer(1)

        # self.t1.start()#开始计时

        self.game.onclick(self.on_click, 1)  # 增加监听
        self.game.onclick(self.on_click_r, 3)
        self.Tstart()

        # t.done()


Mine1 = Mineboard()
t.done()
