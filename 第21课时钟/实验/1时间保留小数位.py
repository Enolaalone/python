import datetime as dt
import turtle as t

window=t.Screen()
a=t.Pen()
def T():#显显示函数

    tm=dt.datetime.today()
    a.clear()
    a.write(f'{tm:%Y-%m-%d %H:%M:%S}',font=('宋体',20,'normal'))
    t.ontimer(T,1000)
T()
window.mainloop()