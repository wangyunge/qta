# -*- coding:utf-8 -*- 
import xlrd
from django.utils.encoding import smart_str, smart_unicode

data=xlrd.open_workbook('贵州移动NPS调研数据-提供研究院.xlsx')
table=data.sheets()[5]
file_object = open('sheet6.txt','wr')
nrow = table.nrows
try:
    for i in range(table.nrows-1):
        file_object.write(smart_str(table.row_values(i+1)[3])+'\n')
finally:
    file_object.close()
        


