def function(a):
    i=0
    sum=0
    while i<=a:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    return sum
print(function(20))