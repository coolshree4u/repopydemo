a=1

def raise_exception(a):
    if type(a) != type('a'):
        raise ValueError("This is not string")

try:
    raise_exception(a)
except ValueError as e:
    print(e)



def TestCase(a,b):
    assert  a <b , "a is greater than b"

try:
    TestCase(2,1)
except AssertionError as e:
    print(e)