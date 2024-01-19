import random as r
import openpyxl

wb = openpyxl.Workbook()


def plus_g():
    a = r.randint(1, 9)
    b = r.randint(1, 9)
    A[f'{a}+{b}='] = a + b


def plus():
    a = r.randint(10, 100)
    b = r.randint(10, 100 - a)
    A[f'{a}+{b}='] = a + b


def diminish():
    a = r.randint(1, 100)
    b = r.randint(1, a)
    A[f'{a}-{b}='] = a - b


def multiply():
    a = r.randint(1, 100)
    b = r.randint(1, 100)
    while a * b > 100:
        a = r.randint(1, 100)
    A[f'{a}x{b}='] = a * b


def divide():
    a = r.randint(1, 100)
    b = r.randint(1, 100)
    while a % b != 0:
        b = r.randint(1, 100)
    A[f'{a}/{b}='] = a // b


def record(a1):
    sheet1['F1'] = '个位加法'
    sheet1['G1'] = '加法'
    sheet1['H1'] = '减法'
    sheet1['I1'] = '乘法'
    sheet1['J1'] = '除法'
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in a1:
        if ('+' in i) and (len(i) <= 4):
            a += 1
            sheet1['F2'] = a
        if ('+' in i) and (len(i) > 4):
            b += 1
            sheet1['G2'] = b
        if '-' in i:
            c += 1
            sheet1['H2'] = c
        if 'x' in i:
            d += 1
            sheet1['I2'] = d
        if '/' in i:
            e += 1
            sheet1['J2'] = e


k = 'y'
n = 0
while k == 'y':
    n += 1
    A = {}
    name = input('姓名')
    sheet = wb['Sheet']
    sheet1 = wb.create_sheet(f'{name}.xlsx')

    for i in range(2):
        divide()
        diminish()
        multiply()

    for i in range(2):
        k = r.randint(0, 1)
        if k == 1:
            plus()
        else:
            plus_g()

    for i in range(2):
        k = r.randint(1, 5)
        if k == 1:
            plus_g()
        if k == 2:
            plus()
        if k == 3:
            divide()
        if k == 4:
            diminish()
        if k == 5:
            multiply()

    B = list(A)
    print(B)
    record(B)

    sheet1[f'A1'] = '题目'
    sheet1[f'B1'] = '正确答案'
    sheet1[f'C1'] = f'{name}的答案'
    sheet1[f'D1'] = f'得分'
    sheet1[f'E1'] = f'总分'
    score = 0
    for i in range(10):
        k = r.randint(0, len(B) - 1)
        print(B[k])
        sheet1[f'A{i + 2}'] = B[k]
        sheet1[f'B{i + 2}'] = A[B[k]]
        answer = int(input('输入结果'))
        sheet1[f'C{i + 2}'] = answer

        if answer == A[B[k]]:
            print('正确')
            sheet1[f'D{i + 2}'] = 10
            score += 10
        else:
            print('错误')
            sheet1[f'D{i + 2}'] = 0

        A.pop(B[k])
        del B[k]
    sheet1[f'E2'] = score

    sheet[f'A{n}'] = name
    sheet[f'B{n}'] = score

    k = input('是否在做一次？y/n')

wb.save('算术.xlsx')
