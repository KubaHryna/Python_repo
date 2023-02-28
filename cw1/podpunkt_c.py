import math


def function(n):
    e2=0
    e1=(1+(1/n))**n
    for x in range(0, n):
        e2 = e2 + 1/math.factorial(x)
    print("e1-math.e wynosi = ", e1 - math.e)
    print("e2-math.e wynosi =", (e2 - math.e))
    print("|e1-math.e| wynosi = ", abs(e1-math.e))
    print("|e2-math.e| wynosi =", abs(e2 - math.e))
    print(e2)


l=int(input("Podaj liczbe całkowitą: "))
function(l)
