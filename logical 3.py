def list():
    a=[3,5,[],4,1,[],2,8]
    i=0
    j=[]
    while i<len(a):
        if a[i]!=[]:
            j.append(a[i])
        i+=1
    print(j)
list()
