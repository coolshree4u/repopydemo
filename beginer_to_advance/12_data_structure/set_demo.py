my_set = set(['one','two','one','one','two','three'])
print(my_set)

my_set1= set(['two','three','four'])
print(my_set1)
print(my_set| my_set1)
print(my_set ^ my_set1)

print(my_set1.add('eight'))
print(my_set1)


print(my_set1.intersection(my_set))
print(my_set.union(my_set1))
print(my_set.difference(my_set1))