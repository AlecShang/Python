#!/usr/bin/python3

import openpyxl
import re


# excel表的表名称
excel_name='2020停车场收明细表'+'.xlsx'
# 工作簿的名称
name='1月份'
test=[]
time=''
pattern = re.compile('(\d{4}[\.\-/年]{1}\d{1,2}[\.\-/月]{1}\d{1,2}[ ]{0,1}\d{2}[:]\d{2}[:]\d{2}).*([\u4E00-\u9FA5]+[A-Z0-9]{6}).*')
book = openpyxl.load_workbook(excel_name)
sheet = book[name]
cells_rows=sheet.max_row
cells_col=sheet.max_column
cells=sheet.values #读取整个sheet
for col in range(cells_col):
    # if cell!='':
        for row in range(cells_rows):
                b=re.findall(pattern,str(sheet.cell(row+1,col+1).value))
                if b!=[] and time!=b[0][0]:
                    if '放行' in str(sheet.cell(row+1,col+1).value):
                        test.append(b[0][0])
                        test.append(b[0][1])
                        test.append('离开时间')
                        time=b[0][0]
                    # if '识别车牌' in str(sheet.cell(row+1,col+1).value):
                    if sheet.cell(row+1,col+1).value[0]=='0':
                        test.append(b[0][0])
                        test.append(b[0][1])
                        test.append('进入时间')
                        time=b[0][0]


#创建excel文档
wb =openpyxl.Workbook()
sheet = wb['Sheet']
sheet['A1'] = '时间'
sheet['B1'] = '车牌号'
sheet['C1'] = '进离操作'
x = 2
for i in range(0,len(test),3):
    sheet['A'+str(x)] = test[i]
    sheet['B'+str(x)] = test[i+1]
    sheet['C'+str(x)] = test[i+2]
    x += 1


wb.save(name+'.xlsx')