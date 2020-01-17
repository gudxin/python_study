import xlrd

#xlrd可对xlsx,xls进行读取
file = 'D:\projects\python_project\python_study\Learn python3 the hard way\Excel\考试成绩\七年级\上学期\七年级第二学期期末考试全县成绩统计表.xlsx'
#file = 'D:\projects\python_project\python_study\Learn python3 the hard way\Excel\考试成绩\七年级\上学期\期末考试前100名.xls'

def read_excel():
	wb = xlrd.open_workbook(filename = file)
	#excel中表个数和表名
	print(wb.sheet_names())
	sheet1 = wb.sheet_by_index(0)
	sheet2 = wb.sheet_by_name('分班')
	#<xlrd.sheet.Sheet object at 0x000000EAB8AEA0B8> <xlrd.sheet.Sheet object at 0x000000EAB8AEA0B8>
	print(sheet1,sheet2)
	#sheet1.name：分班 行数：435  列数：15
	print(sheet1.name,sheet1.nrows,sheet1.ncols)
	for i in range(2,sheet1.nrows):
		rows = sheet1.row_values(i)
		cols = sheet1.col_values(3)
		print(rows)

	#拿第三行表格内容
	rows = sheet1.row_values(2)
	#list中有浮点型和整数型,不能用join转字符串
	#可用str直接转成字符串
	rows_str = str(rows)
		len_rows_str = len(rows_str)
		print(f"len_str={len_rows_str}")
	b = [str(i) for i in rows]
	print(f"b:{b}")
	c = ' '.join(b)
	print(f"c:{c}")
	rows_string = "".join(rows_str)
	print(type(rows))
	print(rows)
	print(type(rows_str))
	print(rows_str)
	print(type(rows_string))
	print(rows_string)


read_excel()

# import pandas as pd
# # import numpy as np
# #
# # s = pd.Series([1,2,3,np.nan,5,6])
# # print(type(s))
# # print(s)


# step one : find all files.xls
import os
path = r'D:\考试成绩'
for i in os.walk(path):
    # tuple
    # print(type(i))
    # #(文件夹路径，文件夹名称，文件夹下的文件)
    # print(i)
    #从tuple中取出文件夹里面的文件,并数出文件个数
    # print("len(i[2]):{}".format(len(i[2])))
    # print(i[2])
    k = 0
    for j in range(len(i[2])):
        if ((".xls" or ".xlsx") and "成绩") in i[2][j]:
            k += 1
            print(i[2][j])
    print(k)



    #转为字符串
    # a = " ".join(i[2])
    # b = a.partition(" ")
    # # print(f"a:{type(a)}")
    # # print(f"a={a}")
    # print(type(b))
    # print(b)

    # if (".xls" or "xlsx") and "成绩" in a:
    #     print(a)

