import random as r


class Mine:
    def __init__(self,x,y):
        self.y=y
        self.x=x
        self.txt='\u25A0'
        self.txt1='\u25A1'
        self.txt2='*'
        self.is_mine=False
        self.status=False
        self.number=0

    def draw(self):
        if not self.status:
            print(self.txt,end='\t')
        else:
            if self.is_mine:
                print(self.txt2,end='\t')
            else:
                if self.number==0:
                    print(self.txt1,end='\t')
                else:
                    print(self.number,end='\t')

    def check(self):
        if self.is_mine:
            print(self.txt2,end='\t')
        else:
            if self.number == 0:
                print(self.txt1, end='\t')
            else:
                print(self.number, end='\t')


class Mines:
    def __init__(self):
        self.n=0
        self.mines=[]
        for i in range(1,11):
            A=[]
            for j in range(1,11):
                A.append(Mine(i,j))
            self.mines.append(A)
        self.create_mine()
        self.show()
        print()
        self.show_check()
        self.run()

    def show(self):
        for i in range(11):
            print(i,end='\t')
        print()
        for i in range(10):
            print(f'{i+1}',end='\t')
            for j in range(10):
                self.mines[i][j].draw()
            print()

    def show_check(self):
        for i in range(11):
            print(i, end='\t')
        print()
        for i in range(10):
            print(f'{i + 1}', end='\t')
            for j in range(10):
                self.mines[i][j].check()
            print()

    def show_mine(self):
        for i in range(10):
            for j in range(10):
                if self.mines[i][j].is_mine:
                    self.mines[i][j].status=True
        self.show()

    def create_mine(self):
        n=0
        while n<10:
            a=r.randint(0,9)
            b=r.randint(0,9)
            if not self.mines[a][b].is_mine:
                self.mines[a][b].is_mine=True
                for x in [-1,0,1]:
                    for y in [-1,0,1]:
                        if 0<=x+a<=9 and 0<=y+b<=9:
                            if x!=0 or y!=0 :
                                self.mines[a+x][b+y].number+=1
                n+=1

    def explore(self,x,y):
        if x<0 or x>9 or y<0 or y>9 or self.mines[x][y].is_mine or self.mines[x][y].status:
            return
        self.mines[x][y].status=True
        self.n+=1
        if self.mines[x][y].number>0:
            return

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    self.explore(x+dx,y+dy)

    def run(self):
        while True:
            position_x=int(input('输入行号'))-1
            position_y=int(input('输入列号'))-1
            if self.mines[position_x][position_y].is_mine:
                self.show_mine()
                print('游戏失败')
                break
            if self.n>=90:
                self.show_mine()
                print('游戏成功')
                break
            self.explore(position_x,position_y)
            self.show()
            print()
            self.show_check()


if __name__ == '__main__':
    mines=Mines()


