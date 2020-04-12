#### Zadanie 1.8 | Kalkulator lat psich
#Zakładamy, że 1 ludzki rok, to 5 lat psich.
#Za pomocą konsoli wczytaj imię i wiek psa.
#Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.

imie = str(input("Podaj imię psa: "))
wiek = int(input("Podaj wiek psa: "))
wiek_1 = wiek * 5
print("Gdyby", imie, "był człowiekiem, miałby", wiek_1, "lat.")