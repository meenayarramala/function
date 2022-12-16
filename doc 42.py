def a(n):
    i=0
    x=[]
    while i<len(n):
        sum=0
        while n[i]>0:
            sum+=n[i]%10
            n[i]=n[i]//10
        x.append(sum)
        i=i+1
    print(x)
a([12, 67, 98, 34])
# a([15, 81, 11, 234])