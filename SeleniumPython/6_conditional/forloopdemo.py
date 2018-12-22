mystring='abcabc'

for c in mystring:
    if c=='a':
        print('A',end=' ')
    else:
        print(c, end=' ')


cars=['bmw','honda','benz']
for item in cars:
    print(item)


nums=[1,2,3]
for num in nums:
    print(num*10)

d={"one":1,"two":2,"three":3}
for item in d:
    print(item+" "+str(d[item]))

for k,v in d.items():
    print(k+" "+str(v))