import faker
import xlwt

data = faker.Faker()

wk = xlwt.Workbook()
ws = wk.add_sheet("Sheet1")


def displaywelcomeMessage():
    print("*****************************************************\n\n")
    print("Welcome to the test data generator by Testing World\n\n")
    print("*****************************************************\n\n")


def enternumberofrecords():
    r = raw_input("Please enter the number of records")
    return r


def selectOptions():
    print("Please select the data which you want to generate\n\n")
    print("Eenter 1 for Full Name")
    print("Eenter 2 for Full Address")
    print("Eenter 3 for Email")
    options = raw_input("Please Enter your choice(Use comma in case of multiple options)")
    return options


def GenerateData(rec, data1):
    r = int(rec)
    li = data1.split(",")
    for i in range(0, r):
        count = 0
        for j in li:
            if j == '1':
                ws.write(i, count, data.name())
                count = count + 1
            elif j == '2':
                ws.write(i, count, data.email())
                count = count + 1
            elif j == '3':
                ws.write(i, count, data.city())
                count = count + 1

        wk.save("td_genration.xlsx")
