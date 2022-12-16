def num(x):
    i=0
    y=str(x)
    while i<len(y):
        if y[i]!="0":
            print(y[i],end="")
        i=i+1
num(int(input("enter the number")))

