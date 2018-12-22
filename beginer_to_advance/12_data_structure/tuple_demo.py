tup =(1,'abc',2,'cde')
tup1= 3,'efg',True

tup2='A'
print(tup2)
print(tup1[1])
print(tup1[0])
print(tup[0:2])

try:
    tup[3] =5
except Exception as e:
    print(e)

tup = tup[0:3] + (5,)
print(tup)

for x in tup:
    print(x)

print(len(tup))
# print(min(tup))
# print(max(tup))