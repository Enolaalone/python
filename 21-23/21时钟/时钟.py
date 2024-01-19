import turtle as t
import datetime


class Needle(t.Turtle):
    def __init__(self,length,color,name):
        super().__init__()
        self.width=10
        self.length=length
        self.color=color

        t.begin_poly()
        t.fd(self.length)
        t.end_poly()
        t.register_shape(name,t.get_poly())
        t.home()
        t.clear()

        self.shape(name)
        self.shapesize(2,1,self.width)

    def renew(self,angle):
        self.seth(angle)


class Wheel(t.Turtle):
    def __init__(self):
        super().__init__()
        self.r=200
        self.hideturtle()
        t.setup(600,600)
        self.draw()


    def move(self,x,y):
        self.pu()
        self.goto(x,y)
        self.pd()

    def draw(self):
        t.tracer(0)
        self.hideturtle()
        self.move(0,self.r)
        for i in range(60):
            if i%5==0:
                self.dot(20)
            else:
                self.dot(5)
            self.pu()
            self.circle(-self.r,6)
            self.pd()
        self.move(0,self.r+13)
        for i in range(12):
            self.pu()
            self.circle(-self.r-30,30)
            self.pd()
            self.write(i+1,align="center",font=('宋体',30,'bold'))
        t.tracer(1)


class Clock:
    def __init__(self):
        self.now=datetime.datetime.now()
        t.hideturtle()
        self.needle_1=Needle(90,'black','秒针')
        self.needle_2=Needle(70,'black','分针')
        self.needle_3=Needle(50,'black','时针')
        self.tick()
        self.wheel=Wheel()
        t.mainloop()

    def tick(self):
        t.tracer(0)
        t.clear()
        self.now=datetime.datetime.now()
        t.pu()
        t.goto(-6,20)
        t.pd()
        t.write(f'{self.now:%Y/%m/%d %H:%M:%S}',align="center",font=('宋体',14,'bold'))
        self.needle_1.renew(-self.now.second*6+180)
        self.needle_2.renew(-6*(self.now.second/60)-self.now.minute*6+180)
        self.needle_3.renew(-30*(self.now.minute/60)-self.now.hour*30+180)
        t.tracer(1)
        t.ontimer(self.tick,1000)


if __name__=="__main__":
    clock=Clock()