file = open("write.txt",'w+')

file.write("Hello I am a string! ")

file.seek(0)
file.write("This")
print(file.read())
file.close()