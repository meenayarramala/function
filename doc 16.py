def table(a):
    i=1
    while i<=n:
        j=0
        while j<=10:
            print(i,"*",j,"=",i*j)
            j=j+1
        i=i+1
        print()
n=int(input("enter the number"))
table(n)