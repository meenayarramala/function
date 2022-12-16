def vote(age):
    if age>=18:
        return "eligible for voting"
    else:
        return "not"
b=int(input("no"))
print(vote(b))