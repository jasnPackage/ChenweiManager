#coding:utf-8
import xlrd
import os
from datetime import datetime
from xlrd import xldate_as_tuple

d = os.path.dirname(__file__)
parent_path = os.path.dirname(d)
data_path = os.path.join(parent_path,'data')

class Excel():
    def __init__(self):
        self.data_path = os.listdir(data_path)

    def interface_info(self):
        for file_name in self.data_path:

            self.data = xlrd.open_workbook(os.path.join(data_path,file_name))
            table = self.data.sheet_by_index(0)
            inf_name = table.row_values(1)[0]
            inf_address = table.row_values(1)[1]
            inf_mode = table.row_values(1)[2]
            # print(inf_name,inf_address,inf_mode)
            return inf_name,inf_address,inf_mode

    def read_excel(self):
        for file_name in self.data_path:
            rbook = xlrd.open_workbook(os.path.join(data_path, file_name))
            sheet = rbook.sheet_by_index(1)
            rows = sheet.nrows
            cols = sheet.ncols
            all_content = []
            for i in range(rows):
                row_content = []
                for j in range(cols):
                    ctype = sheet.cell(i, j).ctype  # 表格的数据类型
                    cell = sheet.cell_value(i, j)
                    if ctype == 2 and cell % 1 == 0:  # 如果是整形
                        cell = int(cell)
                    elif ctype == 3:
                        # 转成datetime对象
                        date = datetime(*xldate_as_tuple(cell, 0))
                        cell = date.strftime('%Y/%m/%d')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    row_content.append(cell)
                all_content.append(row_content)
                print
                '[' + ','.join("'" + str(element) + "'" for element in row_content) + ']'
            print(all_content)
            # return all_content


if __name__ == '__main__':
    dt = Excel()
    dt.interface_info()
    dt.read_excel()
