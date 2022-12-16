
def result(l):
    i=0
    s=0
    while i<len(l):
        d=l[i]
        k=d[::-1]
        if d==k:
            s=s+1
        i=i+1
    return s
print(result(["abc","xyz","aba","1221"]))