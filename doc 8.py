def string(a):
    i=0
    upper=0
    lower=0
    while i<len(a):
        if a[i].isupper():
            upper+=1
        if a[i].islower():
            lower+=1
        i=i+1
    print(upper)
    print(lower)
string('The quick Brow Fox')




# def fun():
#     print('fun')
# print(fun())



# a=100/5
# b=20//3
# print(a*b)