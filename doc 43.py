def fun(a):
    n=int(input("enter the number"))
    i=len(a)-n
    while i<len(a):
        print(a[i])
        i=i+1
fun(['a',1,'2',5,'b','q'])