def printvalues():
    list=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
    b=[]
    i=1
    while i<len(list):
	    b.append(i**2)
	    i+=1
    print(b[:5])
    print(b[-5:])
printvalues()