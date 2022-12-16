def harshad():
    n=int(input("enter the number...."))
    a=n
    rem=0
    sum=0
    while a>0:
        rem=n%10
        sum=sum+rem
        a=a//10
    if n%sum==0:
        print("this is harshad number.")
    else:
        print("this is not harshad number.")
harshad()
