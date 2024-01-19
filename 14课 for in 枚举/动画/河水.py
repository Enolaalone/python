import random
import turtle
def move(x,y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
def river(x,y):
    move(x,y)
    turtle.color('skyblue')
    turtle.begin_fill()
    for i in range(2):
        turtle.fd(600)
        turtle.right(90)
        turtle.fd(1200)
        turtle.right(90)
    turtle.end_fill()
turtle.tracer(0)
#river(-300,600)
turtle.tracer(1)
turtle.done()

a=random.randint(0,1)
print(a)