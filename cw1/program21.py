import math
a = 5.51
print(math.ceil(a))
print(math.floor(a))
print(round(a))
x = 5.5672
y = 5
a = 4
n = 6
def function (x, y):
    if isinstance(x, int) and isinstance(y, int):
        wynik = x % y
        print(wynik)
    elif isinstance(x, float) or isinstance(y, float):
        wynik = math.fmod(x, y)
        print(wynik)

def function2 (a, n):
            for i in range(2, n+1):
                print(math.log(a, i), end=" | ")


def potega(a):
    print(math.exp(a))
    print(math.e ** a)
    print(math.pow(math.e, a))

function(x, y)
print("Logarytmy:")
function2(a, n)
potega(a)