list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list3 = []
for x in range(len(list1)):
    list3.append(list1[x]+list2[x])

print(list3)
months = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień",
          "wrzesień","październik", "listopad", "grudzień"]
miesiace = ["maj", "luty", "styczeń"]
def function(x):
    if x == "styczeń":
        return 0
    elif x == "luty":
        return 1
    elif x == "marzec":
        return 2
    elif x == "kwiecień":
        return 3
    elif x == "maj":
        return 4
    elif x == "czerwiec":
        return 5
    elif x == "lipiec":
        return 6
    elif x == "sierpień":
        return 7
    elif x == "wrzesień":
        return 8
    elif x == "październik":
        return 9
    elif x == "listopad":
        return 10
    elif x == "grudzień":
        return 11


miesiace.sort(key=function)
print(miesiace)

nazwiska = ["Ignaciuk", "Igielski", "Zawiślak", "Zaręba", "Kapela",
            "Deręgowski", "Ślusarz", "Raj", "Mączka", "Jaroń"]
litera = "X"
newlist = []
def function2(lista,litera):
    for i in range(0, len(lista)):
        if lista[i][0] > litera:
            newlist.append(lista[i])



function2(nazwiska, litera)
print(newlist)

def function3(lista):
    lista = [x for x in lista if len(x) > 6]
    print(lista)

function3(nazwiska)

liczby = [1, 2, 3, 6, 4, 5]
liczby2 = [1, 9, 3, 6, 2, 15]

def check_if_sorted(zbior):
    for i in range(len(zbior)-1):
         if (zbior[i] > zbior[i + 1]):
            return False
         else:
                continue
    return True


print(check_if_sorted(liczby))

print(check_if_sorted(liczby2))

liczby3 = [1, 2, 3, 4]

liczby3 = [pow(x, 3) for x in liczby3]
print(liczby3)

list = []

for i in range(0, 6):
    li_rz = float(input("Podaj 6 liczb rzeczywistych: "))

    list.append(li_rz)

n1 = float(input("Podaj liczbe która ma być zmieniona: "))
n2 = float(input("Podaj liczbe na jaką chcesz zmienić: "))

def func(list, n1, n2):
    for x in range(len(list)):
        if list[x] == n1:
            list[x]=n2

    return list


print(func(list, n1, n2))
