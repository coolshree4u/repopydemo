"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt as test
from car_module.module_car import info

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(test(100))


m = ModulesDemo()
info("TATA","Indica-Vista")
m.builtin_modules()