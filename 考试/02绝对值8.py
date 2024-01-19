a=float(input('输入一个数'))
if a<0:
    b=float(int(a))
    c=b-a
    print("%.0f"%-b)
    print(c)
else:
    b = float(int(a))
    c = a-b
    print("%.0f" % b)
    print(c)