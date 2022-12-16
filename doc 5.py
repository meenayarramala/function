def list(l):
    i=0
    b=[]
    while i<len(l):
        if l[i] not in b:
            b.append(l[i])
        i=i+1
    return b
print(list([1,2,3,3,3,3,4,5]))