def printData():
    print("This is testing world")


def addition(a,b=10):
    print("Inside Addtion")
    c=a+b
    print("Addition of given argument "+str(c))


def substraction(a,b):
    print("Inside Addtion")
    c=a-b
    print("Substraction of given argument "+str(c))
    return c

printData()
addition(10,20)
z=substraction(100,50)
printData()
addition(int(z))