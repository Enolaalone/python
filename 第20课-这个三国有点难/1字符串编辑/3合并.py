import openpyxl as o
#表格读入
wb=o.load_workbook('文本.xlsx')
sheet=wb['文本.xlsx']

#确定数目
with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    b=f.read()
    print(len(b))

with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    for i in range(len(b)):#一个一个读取
        a=f.read(1)
        print(a)
        sheet[f'A{i + 1}'] = i + 1  # 序号
        sheet[f'B{i + 1}'] = a  # 字符
        sheet[f'C{i + 1}'] = bin(ord(a))  # 16进制码
wb.save('文本.xlsx')


