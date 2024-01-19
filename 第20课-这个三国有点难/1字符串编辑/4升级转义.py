import openpyxl as o
#表格读入
wb=o.load_workbook('文本1.xlsx')
sheet=wb['文本.xlsx']
A=['\a','\b','\f','\n','\r','\t','\v','\\','\'','\"','\?','\ddd',' ']#特殊字符
B=[r'\a',r'\b',r'\f',r'\n',r'\r',r'\t',r'\v',r'\\',r'\'',r'\"',r'\?',r'\ddd',r'\0']
#确定数目
with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    b=f.read()
    print(len(b))

with open('新建 文本文档.txt','r',encoding='utf-8') as f:
    for i in range(len(b)):#一个一个读取
        a=f.read(1)
        a1=repr(a)
        print(a)
        sheet[f'A{i + 1}'] = i + 1  # 序号
        if a not in A:
            sheet[f'B{i + 1}'] = a  # 字符
            print(0)
        else:
            print(1)
            k=A.index(a)
            sheet[f'B{i + 1}'] = B[k]  # 非字符
        sheet[f'C{i + 1}'] = bin(ord(a))  # 二进制码

wb.save('文本1.xlsx')


