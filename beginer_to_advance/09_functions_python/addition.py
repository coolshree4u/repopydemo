def add(a, b):
    c = a + b
    return c

def default_param(a, b=4, c=5):
    return a+b+c

def scope(a):
    a = a+1
    print(a)
    return a

def f(a):
    def g(b):
        return a*b
    return g

print(f(2)(5))


print(default_param(10))

print(add(12,5))

print(scope(10))