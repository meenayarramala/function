def upperlower(string):
    u=0
    l=0
    i=0
    while i<(len(string)):
        if ord (string[i])>=97 and ord (string[i])<=122:
            l+=1
        elif ord(string[i])>=65 and ord(string[i])<=90:
            u+=1
        i+=1
    print('Lower case characters=:',l)
    print('Upper case characters="',u)
string='MY nAme iS MeEnA'
upperlower(string)