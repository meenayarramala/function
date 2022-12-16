def function(a):
    i=0
    p=0
    n=0
    while i<len(a):
        if a[i]>0:
            p+=1
        else:
            n+=1
        i=i+1
    print("positive",p)
    print("negative",n)
function([2, -7, 5, -64, -14])