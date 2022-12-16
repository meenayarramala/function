days=int(input("enter the no:"))
if days<=5:
    charge1=5*2
    print("total cost",charge1)
elif days>5 and days<=10:
    charge2=(5*2)+(days-5)*3
    print("total cost",charge2)
elif days>=10 and days<=15:
    charge3=(5*2)+(5*3)+(days-10)*4
    print("total cost",charge3)
elif days>15:
    charge4=(5*2)+(5*3)+(5*4)+(days-15)*5
    print("total cost",charge4-days)