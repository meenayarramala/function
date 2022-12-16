def fun(a):
    i=0
    b=[]
    while i<len(a):
        if a[i]%2==0:
            d=a[i]*100
        else:
            d=a[i]*-1
        i+=1
        b.append(d)
    return d
print(fun([22]))
            