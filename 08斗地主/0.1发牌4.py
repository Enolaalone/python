import turtle as t
t.pensize(0.2)
t.pencolor('black')

t.begin_fill()
for i in range(2):
    t.fd(90)
    t.left(90)
    t.fd(60)
    t.left(90)
t.end_fill()
for i in range(2):#画出带框的牌
    t.fd(90)
    t.left(90)
    t.fd(60)
    t.left(90)