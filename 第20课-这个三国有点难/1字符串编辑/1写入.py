import openpyxl as o
wb=o.load_workbook('文本.xlsx')
sheet=wb['文本.xlsx']

A='13!@#$%^&国aA'#使用字符串
for i in range(len(A)):
    sheet[f'A{i+1}']=i+1#序号
    sheet[f'B{i+1}']=A[i:i+1]#字符
    sheet[f'C{i+1}']=bin(ord(A[i:i+1]))#16进制码
    print(type(bin(ord(A[i:i + 1]))))#确定类型
    print(bin(ord(A[i:i+1])))
    print(len(bin(ord(A[i:i+1]))))
wb.save('文本.xlsx')