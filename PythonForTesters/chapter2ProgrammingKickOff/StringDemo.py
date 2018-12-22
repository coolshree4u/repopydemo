print("Hello My name is 'Testing World'")
print('Hello My name is "Testing World"')


print("This is Testing' Book")

print("""
        This is Book for 
        Testing
        """)


s="Testing "
s1="World"

print(s+s1)
print(s*10)
print(s[0])
print(s[1:4])

print(s[1:])
print(s[:5])


s="   Testing    "
print(s)
print(s.lstrip())
print(s.rstrip())
print(s.lstrip())


print(s.replace('es','ES' ))


s1='testing'
s2='TESTING'

if s1==s2:
    print("Compared.")
else:
    print("Not Compared.")