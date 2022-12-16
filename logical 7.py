# def fun(a):
#     i=0
#     j=-1
#     b=[]
#     while i<len(a):
#         c=a[i][j]
#         b.append(c)
#         i+=1
#     print(b)
# fun(a=["mani","jyo"])

def function(a):
    i=0
    c=[]
    while i<len(a):
        b=a.count(a[i])
        if a[i] not in c:
            c.append(a[i])
            print(a[i]+str(b),end="")
        i+=1
function("mani")