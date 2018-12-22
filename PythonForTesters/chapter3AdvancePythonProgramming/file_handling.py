f= open("data.txt",'a+')
print(f.read())
print(f.write("We are adding another line\n"))
print(f.tell())

print(f.seek(100))