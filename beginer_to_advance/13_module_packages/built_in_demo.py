import copy
import math as mt
import cmath as cmt
import random as ran
import sys

print(dir(mt))
print(dir(cmt))
print(ran.random()%10)
print(sys.path)

my_dict={'item':'shirt','size':'medium','price':50}
my_dict1=copy.deepcopy(my_dict)

print(my_dict)
print(my_dict1)
my_dict['item']='Tshirt'

print(my_dict1)