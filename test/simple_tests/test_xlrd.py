from Lamia.Lamia.libs import xlrd
import os

pathxls = os.path.join(os.path.dirname(__file__), '04_Infralineaire.xlsx')

book = xlrd.open_workbook(pathxls)

sheets = book.sheets()
print(sheets)

for sheet in sheets:
    print(sheet.name)
    print(sheet.ncols, sheet.nrows)

    print(sheet.col(0))

    if True:
        for row in range(sheet.nrows):
            print(type(sheet.row(row)))
            print(sheet.row(row))
            for cel in sheet.row(row):
                print(cel)
            print(sheet.cell_value(row, 0), sheet.cell_type(row, 0))



