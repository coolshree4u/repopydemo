import faker
import xlwt
data = faker.Faker()

for i in range(1,11):
    print(data.name()+"  "+data.email()+"  "+data.city())

wk= xlwt.Workbook()
ws=wk.add_sheet("Sheet1")

for i in range(0,1000):
    ws.write(i,0,data.name())
    ws.write(i,1,data.email())
    ws.write(i,2,data.city())


wk.save("test_data.xlsx")

