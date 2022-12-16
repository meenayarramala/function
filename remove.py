def fun():
    a=int(input("enter the number.."))
    i=0
    while i<a:
        if a%10==0:
            a=a//10
        i+=1
    print(a)
fun()
