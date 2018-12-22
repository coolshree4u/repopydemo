import os
from shutil import copyfile
folder_path = '/home/shreeprasadpatil/project/PythonDev/SeleniumPython/images_demo/test'

dictionary={}
count=0
for data_file in sorted(os.listdir(folder_path)):
    count+=1
    print(str(count)+" "+data_file)
    dictionary[count]=data_file

print(dictionary)

file_number=int(input("Enter file number : "))
copyfile('/home/shreeprasadpatil/project/PythonDev/SeleniumPython/images_demo/test/'+dictionary.get(file_number), '/home/shreeprasadpatil/project/PythonDev/SeleniumPython/images_demo/test2/'+dictionary.get(file_number))