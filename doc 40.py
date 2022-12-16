def fun(n):
    a=""
    while n>0:
        b=n%10
        a=str(b**2)+a
        n=n//10
    print(a)
n=int(input("enter the number"))
fun(n)