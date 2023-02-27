import math
lista = []
for i in range(0, 14):
    lista.append(math.pow(i, 5))
print(lista)

lista2 = []
for i in range(1, 20):
    lista2.append(math.factorial(i))
print(lista2)

lista3 = []
for i in range(0, 20):
        lista3.append(math.pow(math.e, i))

print(lista3)

nazwiska = ["Ignaciuk", "Igielski", "Zawiślak", "Zaręba", "Kapela", "Deręgowski", "Ślusarz", "Raj", "Mączka", "Jaroń"]
dlugosc_nazwisk = []
print(len(nazwiska))
for i in range(0, len(nazwiska)-1):
    dlugosc_nazwisk.append(len(nazwiska[i]))

print(dlugosc_nazwisk)

