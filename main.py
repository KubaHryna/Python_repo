import math
b=100
x=int(input("podaj liczbe całkowita: "))
if x > b:
    print("n is too large")
elif x < b:
    for y in range(x+1):
        for z in range(x+1):
            print(y," ",z," ",x*z)


