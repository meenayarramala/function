def even():
    a=[2,4,6,18,10,67,75]
    b=[6,19,24,12,3,87]
    i=0
    while i<len(a):
        if a[i]%2==0 and b[i]%2==0:
            print("both are even")
        else:
            print("both are not even")
        i+=1
even()