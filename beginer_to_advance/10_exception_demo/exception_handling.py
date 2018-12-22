# print(5/0)



# file = open('file','r')


try:
    a = 5/0
except Exception as e:
    print(e)

try:
    n = int(input("Enter an integer: "))
except ValueError:
    print("This is not an integer")
