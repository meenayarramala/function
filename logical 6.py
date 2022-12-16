def li():
    a=[[],2,[],4,[],6,[],8,[],10]
    i=0
    b=[]
    c=[]
    while i<len(a):
        if i%2==0:
            b.append(a[i])
        elif i%2!=0:
            c.append(a[i])
        i=i+1  
    print(b)  
    print(c) 
li()  