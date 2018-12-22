f =  lambda x,y: x+y
test = lambda c: lambda a, b: lambda d: (c * (a+b)) %d

print(test(2)(4,3)(11))
print(f(2,3))