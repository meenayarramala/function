def gen(age):
    if age<14:
        print(age,"Kids drink toddy")
    elif 14<=age and age<18:
        print(age,"teens drink coke")
    elif 18<=age and age<21:
        print(age,"Young adults drink beer")
    elif 21<=age and age<30:
        print(age,"Adults drink whisky")
    else:
        print("drink whatever they want")
gen(20)
