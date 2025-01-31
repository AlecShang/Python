import xlrd

data = xlrd.open_workbook('test.xls')  # 打开xls文件

table = data.sheets()[0]  # 打开第一张表

nrows = table.nrows  # 获取表的行数

# 循环逐行输出

for i in range(nrows):

    if i == 0:  # 跳过第一行

        continue

    print table.row_values(i)[:13]  # 取前十三列数据


import xlrd

# 打开一个xls文件

workbook = xlrd.open_workbook('test.xls')

# 抓取所有sheet页的名称

worksheets = workbook.sheet_names()

print('worksheets is %s' % worksheets)

# 定位到sheet1

worksheet1 = workbook.sheet_by_name(u'Sheet1')


"""

#通过索引顺序获取

worksheet1 = workbook.sheets()[0]

#或

worksheet1 = workbook.sheet_by_index(0)

"""

"""

#遍历所有sheet对象

for worksheet_name in worksheets:

worksheet = workbook.sheet_by_name(worksheet_name)

"""


# 遍历sheet1中所有行row

num_rows = worksheet1.nrows

for curr_row in range(num_rows):

row = worksheet1.row_values(curr_row)

print('row%s is %s' % (curr_row, row))

# 遍历sheet1中所有列col

num_cols = worksheet1.ncols

for curr_col in range(num_cols):

col = worksheet1.col_values(curr_col)

print('col%s is %s' % (curr_col, col))

# 遍历sheet1中所有单元格cell

for rown in range(num_rows):

for coln in range(num_cols):

cell = worksheet1.cell_value(rown, coln)

print cell
