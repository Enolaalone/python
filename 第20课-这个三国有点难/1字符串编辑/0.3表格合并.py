import openpyxl as o
#表格读入
wb=o.load_workbook('文本3.xlsx')
sheet=wb['文本.xlsx']

A='13!@#$%^&国aA\n(&*^^$#'#使用字符串
#for i in range(len(A)):
wb.save('文本3.xlsx')


