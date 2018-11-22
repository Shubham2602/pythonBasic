# Reading an excel file using Python 
import xlrd 

global dict
# Give the location of the file 
loc = ("C:/Users/Admin/Desktop/TestData/MappingsheetForMIDs.xlsx") 
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

def readExcel(row,col):
    return sheet.cell_value(row, col)

for i in range(1,sheet.nrows):
    c = {readExcel(i,1):readExcel(i,0)}
    dict.update(c)

for k,v in dict.items:
    print(k, " ", v)
