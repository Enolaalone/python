import turtle as t
a={'红心A': '♥\nA', '红心2': '♥\n2', '红心3': '♥\n3', '红心4': '♥\n4', '红心5': '♥\n5', '红心6': '♥\n6', '红心7': '♥\n7',
    '红心8': '♥\n8', '红心9': '♥\n9', '红心10': '♥\n10', '红心J': '♥\nJ', '红心Q': '♥\nQ', '红心K': '♥\nK', '方块A': '♦\nA',
    '方块2': '♦\n2', '方块3': '♦\n3', '方块4': '♦\n4.', '方块5': '♦\n5', '方块6': '♦\n6', '方块7': '♦\n7', '方块8': '♦\n8',
    '方块9': '♦\n9', '方块10': '♦\n10', '方块J': '♦\nJ', '方块Q': '♦\nQ', '方块K': '♦\nK', '梅花A': '♣\nA', '梅花2': '♣\n2',
    '梅花3': '♣\n3', '梅花4': '♣\n4', '梅花5': '♣\n5', '梅花6': '♣\n6', '梅花7': '♣\n7', '梅花8': '♣\n8', '梅花9': '♣\n9',
    '梅花10': '♣\n10', '梅花J': '♣\nJ', '梅花Q': '♣\nQ', '梅花K': '♣\nK', '黑桃A': '♠\nA', '黑桃2': '♠\n2', '黑桃3': '♠\n3',
    '黑桃4': '♠\n4', '黑桃5': '♠\n5', '黑桃6': '♠\n6', '黑桃7': '♠\n7', '黑桃8': '♠\n8', '黑桃9': '♠\n9', '黑桃10': '♠\n10',
    '黑桃J': '♠\nJ', '黑桃Q': '♠\nQ', '黑桃K': '♠\nK', '小王': 'jo\nke', '大王': 'JO\nKE'}
b=input('牌名')
t.hideturtle()
t.pensize(3)
def move(x,y):
    t.up()
    t.goto(x,y)
    t.down()


def card(pai):
    move(-150,225)
    for i in range(2):
        t.fd(300)
        t.right(90)
        t.fd(450)
        t.right(90)
    t.right(90)
    t.fd(200)
    if ('红' or '方') in b:
        t.pencolor('red')
        t.write(pai, font=('宋体', 75, 'normal'))
    else:
        t.write(pai, font=('宋体', 75, 'normal'))

t.tracer(0)
card(a[b])
t.tracer(1)
t.done()