
from turtle import *
"""绘制五角星,大小可变"""
def wujiaoxing(size):
    for i in range(6):
        forward(size)
        right(144)

"""绘制红色矩形"""
color("red" ,"red")
begin_fill()
forward(192)
left(90)
forward(128)
left(90)
forward(192)
left(90)
forward(128)
end_fill()
"""绘制第一个大五角星"""
up()
goto(30 ,115)
down()
color("yellow" ,"yellow")
begin_fill()
left(20)
wujiaoxing(30)
end_fill()
"""绘制第一个小五角星"""
up()
goto(55 ,110)
down()
color("yellow" ,"yellow")
begin_fill()
right(10)
wujiaoxing(10)
end_fill()
"""绘制第二个小五角星"""
up()
goto(60 ,100)
down()
color("yellow" ,"yellow")
begin_fill()
left(40)
wujiaoxing(10)
end_fill()
"""绘制第三个小五角星"""
up()
goto(70 ,87)
down()
color("yellow" ,"yellow")
begin_fill()
right(30)
wujiaoxing(10)
end_fill()
"""绘制第四个小五角星"""
up()
goto(50 ,70)
down()
color("yellow" ,"yellow")
begin_fill()
right(20)
wujiaoxing(10)
end_fill()

done()