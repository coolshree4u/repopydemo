def factorial(n):
    if n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(10))



def sum(n):
    if n ==1:
        return 1
    else:
        return n +sum(n-1)

def tail_sum(n,accumulator=0):
    if n==0:
        return accumulator
    else:
        return tail_sum(n-1, accumulator+n)

print(tail_sum(20))