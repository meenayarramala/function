def fun(a):
    i=0
    b=[]
    while i<(a):
        n=int(input("enter the number"))
        b.append(n)
        i=i+1
    print(b)
    j=0
    while j<len(b):
        if b[j]%2==0:
            print("even")
        else:
            print("odd")
        j=j+1
fun(7)

