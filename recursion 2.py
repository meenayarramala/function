def sum(a):
    if len(a)==1:
        return a[0]
    else:
        return a[0]+sum(a[1:])
print(sum([2,4,5,6,7]))




