def primeornot():
    num=int(input("Enter a number....."))
    f=0
    i=2
    while i <=num:
        if num%i==0:
            f=1
            break
        i=i+1
    if f==0:
        print("The is a PRIME number")
    else:
        print("The  is not a PRIME number")
primeornot()  

