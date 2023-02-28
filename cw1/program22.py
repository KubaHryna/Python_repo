napis = "He difficult contented we determine ourselves me am earnestly."

def parzyste_indeksy(napis):
    print(napis[::2])


parzyste_indeksy(napis)
def last_letters(napis, n):
     print(napis[len(napis)-n:])


n = int(input("\nPodaj ile ostatnich znaków z tekstu ma wypisać: "))
last_letters(napis,n)

def odwrocenie(napis):
    print(napis[::-1])

print("\nTwoj odwrocony napis to: \n")
odwrocenie(napis)

n1 = str(input("Podaj pierwszy tekst: \n"))
n2 = str(input("Podaj drugi tekst: \n"))

def dluzszy(n1, n2):
    if len(n1)>len(n2):
        print("Ten tekst jest dluzszy: ", n1 )
    elif len(n2)>len(n1):
        print("Ten tekst jest dluzszy: ", n2 )


dluzszy(n1,n2)

s1 = str(input("Podaj swoje imie: \n"))
s2 = str(input("Podaj swoją datę urodzenia \n"))

print(f'My name is {s1}\nMy date of birth is {s2}')