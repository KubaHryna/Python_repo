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
word1="abccba"
word2="dgjuiafja"
def palindrom(word):
    for i in range(0, len(word)):
        for j in range(len(word), 0):
            if(word[i] != word[j]):
                    return False

            return True



print(palindrom(word1))