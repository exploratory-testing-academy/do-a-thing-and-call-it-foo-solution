import xlrd

class ExcelRef:

    def extract_cell_classic(number):
        loc = ("ref.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        return sheet.cell_value(number, 1)

    def extract_cell_simplified(number):
        loc = ("ref.xls")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        return sheet.cell_value(number, 5)