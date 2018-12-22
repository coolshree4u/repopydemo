age = input("How old are you?")
print(age)


file = open('test.txt','r')
print(file.read(5))
file.seek(5)
print(file.tell())


for line in file:
    print(line)

print("File name is "+ file.name)
print("is Closed "+str(file.closed))
print("Mode "+ file.mode)

file.close()

