for i in range(1,10):
    print(i)

for i in range(0,12,2):
    print(i)


string = 'String traversal!'

for i in range(len(string)):
    print(string[i])

for char in string:
    print(char)


for i in  range(1,11):
    print("{:<3}|".format(i), end="")

    for j in range(1,11):
        print("{:>4}".format(i*j), end="")

    if i==1:
        print("\n{:#^44}|".format(""), end="")

    print("")