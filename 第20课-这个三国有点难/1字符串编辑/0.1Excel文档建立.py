import openpyxl as o
wb=o.Workbook()#创建工作簿
wb.create_sheet('文本3.xlsx')
wb.save('文本3.xlsx')#保存