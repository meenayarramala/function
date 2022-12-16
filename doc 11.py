def range(min,max,step):
    b=[]
    while min<=max:
        b.append(min)
        min+=step
    print(b)
range(2,10,2)