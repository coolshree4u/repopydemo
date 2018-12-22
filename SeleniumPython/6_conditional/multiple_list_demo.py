l1=[1,2,3]
l2=[6,7,8,20,30,40]

for a,b in zip(l1,l2):
    print(a,b)

    if a>b:
        print(a)
    else:
        print(b)