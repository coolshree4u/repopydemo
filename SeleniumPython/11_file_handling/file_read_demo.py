"""
File I/O
'w' -> Write-Only Mode
'r' -> Read-only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""


my_file = open("read_demo.txt", "r")

print(str(my_file.read()))
print("*"*40)

my_file.close()

my_file = open("read_demo.txt", "r")
print(str(my_file.readline()))