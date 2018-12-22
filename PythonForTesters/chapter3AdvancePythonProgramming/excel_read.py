import xlrd
import xlwt

wk = xlrd.open_workbook('test_data.xlsx')
print(wk.sheets())
print(wk.nsheets)

ws = wk.sheet_by_index(0)
print(ws.nrows)

c1 = ws.cell(0, 0)
print(c1.value)

ww = xlwt.Workbook()
wr = ww.add_sheet("Sheet1")
wr.write(0,1,"Dataentry")
ww.save("generated.xlsx")
