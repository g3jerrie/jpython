# Finding greater of three numbers

print("Enter 3 number to compare...")
x = int(input("First Number.."))
y = int(input("Second Number.."))
z = int(input("Third Number.."))
##if(x>y):
##    if(x>z):
##        print(x," is the greater number")
##    else:
##        print(z," is the greater number")
##if(y>z):
##    print(y, " has the highest value")
##else:
##    print(z, " has the highest value")

if(x>y and x>z):
    print(x," is the greater number")
elif(y>z and y>x):
    print(y," is the greater number")
else:
    print(z," is the greater number")

## If the first value is greater and is greater than 150, add 10 to the value


if(x>y):
    print(x," is greater")
    if(x>150):
        x=x+10
        print("Enhanced x: ",x)
else:
    print(y," is greater")

##pass

if(x>200):
    print("Do somthing")
else:
    pass
