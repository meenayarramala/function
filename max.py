def max(a,b,c):
    if a>b:
        if a>c:
            print(a,"it is largest")
        else:
            print(c,"it is largest")
    else:
        if b>c:
            print(b,"it is largest")
        else:
            print(c,"it is largest")

A=int(input("enter the number...."))
B=int(input("enter the number...."))
C=int(input("enter the number...."))
max(A,B,C)
