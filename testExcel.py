from tkinter.ttk import Style
import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0, label='start class')
workbook.save('ExcelTest.xls')
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Times New Roman'
font.bold = True
font.underline = True
font.italic = True
style.font = font

worksheet.write(1, 0, '带格式的单元格', style)
worksheet.col(0).width = 5000
workbook.save('ExcelTest.xls')
