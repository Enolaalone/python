import math
# ------算数实验----
a = 98 + 6
print('%d' % a)  # --------%d 表示整数  用a的值替代%d

h = 9 / 2.8
print('%f' % h)  # ---%f表示浮点数，
print('%.2f' % h)  # -----%f  表示在后面的浮点数填在这里   .2表示保留两位小数
print(f'{h:.2f}')  # format 等价形式


c = math.tan(45*math.pi/180)#仅支持弧度制

print(c)
e = math.sqrt((60) ** 2 + (120) ** 2)

d = math.degrees(math.atan(1))  # degree 中是弧度制
print(e)
print(d)
# for i in range(4):
#     print(i)
