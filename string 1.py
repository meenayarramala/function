def string():
    sentence="NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
    a=' '
    b=[]
    i=0
    while  i<len(sentence):
        if sentence[i]==" ":
            b.append(a)
            a=" "
        else:
            a+=sentence[i]
        i+=1
    if a:
        b.append(a)
    print(b)
string()