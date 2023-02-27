import math
x = int(input("Podaj liczbe całkowitą: "))
y = int(input("Podaj drugą liczbę całkowitą: "))
q = math.gcd(x, y)
x /= q
y /= q
print(x, "/", y)
