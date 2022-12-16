def fun(a):
    i=0
    while i<len(a):
        if a[i]%2==0:
            return "True"
        else:
            return "False"
        i=i+1
# print(fun([2,4,6,8]))
print(fun([2,4,6,8]))