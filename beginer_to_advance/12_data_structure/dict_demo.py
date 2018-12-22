my_dict = {'key':'value',('K','E','Y'):5}
my_dict1 = {x:x +1 for x in range(10)}

print(my_dict)
print(my_dict1)


print(my_dict.keys())
print(my_dict.values())
print(my_dict.clear())
print(my_dict)



#Shallow_copy example

my_dict={'item':'shirt','size':'medium','price':50}
my_dict1=my_dict

print(my_dict)
print(my_dict1)
my_dict['item']='Tshirt'

print(my_dict1)