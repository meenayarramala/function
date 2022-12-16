def string(a):
    i=len(a)
    b=" "
    while i>0:
        b=b+a[i-1]
        i=i-1
    return b
print(string("1234abcd"))