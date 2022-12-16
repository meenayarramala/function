def prime(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count+=1
        i=i+1
    if count==2:
        print("prime num")
    else:
        print("not a prime num")
num=int(input("enter the number"))
prime(num)

