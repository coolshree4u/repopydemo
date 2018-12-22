list1=[1,'abc',(1,2)]
print(list1)
print(2 in list1)

print(list1 == [1,'abc',(1,2)])
print(list1[:2])



print(list(map(lambda x: x**2 + 3*x +1,  [1,2,3,4])))


print(list(filter(lambda x: x<4,[1,2,3,54432,354,45,6,75,3,2])))