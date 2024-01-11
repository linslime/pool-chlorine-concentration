import math
from xlutils.copy import copy
import xlrd as xr

def function(t):
    return -0.1129503 * math.pow(10,t/5 - 5.4) * 0.4 + -0.000367024 * 521
step = 0.001
T = 33
list = []
while T < 40:
    list.append([T,function(T)])
    T += step
print(list)

# file = "D:\\Desktop\\two.xls"
# oldwb = xr.open_workbook(file)
# newwb = copy(oldwb)
# newws = newwb.get_sheet(-1 + 3)
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         newws.write(i + 1, j + 1, list[i][j])  # 行，列，数据
# newwb.save(file)