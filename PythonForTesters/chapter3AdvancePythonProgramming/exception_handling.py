inp= raw_input("Please enter your marks  ")
inp1 = raw_input("Please enter another marks  ")
try:
    print int(inp)+int(inp1)
except:
    print("Your input is incorrect.....")
finally:
    print("Closing this execution")