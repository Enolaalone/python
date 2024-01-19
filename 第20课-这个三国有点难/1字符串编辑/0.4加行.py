import openpyxl as o
#表格读入
wb=o.load_workbook('文本3.xlsx')
sheet=wb['文本3.xlsx']
sheet.insert_rows(2)
sheet.insert_cols(2)

wb.save('文本3.xlsx')