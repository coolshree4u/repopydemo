tu=(23,45.56,'String demo')
tu1=(23,45.56,'String demo')
print(tu)
print(tu[0:2])
print(len(tu))
#Tupple can not be modified directly like tu[0]=345
#This will throw an error
print(cmp(tu,tu1))

print(tu1+tu)

