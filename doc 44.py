def fun(a):
    n=int(input("enter the number"))
    j=-1
    while j>=-(len(a)-n):
        print(a[j])
        j=j-1
fun(['a',1,'2',5,'b','q'])