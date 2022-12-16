def add(a):
    i=0
    firstmax=0
    secondmax=0
    while i<len(a):
        if a[i]>firstmax:
            secondmax=firstmax
            firstmax=a[i]
        elif a[i]>secondmax:
            secondmax=a[i]
        i=i+1
    print(firstmax+secondmax)
a=[99,2,2,23,19]
add(a)



# a=[1,2,3,4]
# a[1:3]=["watwemelon"]
# print(a)


# a=[1,2,3,4]
# print(a[::2])


a="apple"
a="banana"
print("apple"+a)
print("banana"+a)