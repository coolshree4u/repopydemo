class Student(object):

    '''Student'''
    number_of_students =0

    def __init__(self,name, index):
        self.name=name
        self.index =index
        Student.number_of_students +=1

    def __del__(self):
        Student.number_of_students -= 1


s1=Student('Shree',12345)
s2=Student('test',12675)
print(Student.number_of_students)
print(s1.number_of_students)
print(s2.number_of_students)

del s1
print(Student.number_of_students)