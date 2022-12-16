def function(weight,height):
    bmi=(weight/(height*height))*1000
    if bmi<=18.5:
        c="underweight"
        return c
    elif bmi<=25.0:
        c="normal"
        return c
    elif bmi<=30.0:
        c="overweight"
        return c
    elif bmi>30:
        c="obese"
        return c
weight=int(input("enter the number"))
height=int(input("enter the number"))
print(function(weight,height))



# a=4/5
# b=5//4
# print(a*b)