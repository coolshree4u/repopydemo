no = raw_input('Please enter number')
if int(no)<0 or int(no)>100:
    print('This is invalid number')
elif int(no)%2==0:
    print("This is Even Number")
else:
    print("This is Odd Number")
