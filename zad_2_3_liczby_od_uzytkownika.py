# ### Zadanie 2.3
# Napisz program, który odczytuje od użytkownika wiele liczb.
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
# - liczba podanych liczb (ile sztuk),# - suma,# - średnia,# - minimum# - maksimum
# NIE używaj funkcji wbudowanych!
liczby = []
ilosc = 0
suma = 0
min = 0
max = 0

while True:
    liczba = input("Podaj liczbę całkowitą, jeśli chcesz skączyć i zobaczyć wynik, wprowadź \"x\": ")

    if liczba != "x":
        liczba = int(liczba)
        liczby.append(liczba)
        ilosc += 1
        suma = suma + liczba
        if int(min) > int(liczba):
           min = int(liczba)
        if int(max) < int(liczba):
           max = int(liczba)

    if ilosc == 1:
        min = int(liczba)
        max = int(liczba)
        continue

    if liczba == "x":
        print(f"Ilość podanych liczb: {ilosc} \nSuma : {suma}\nMin : {min}\nMax : {max} "
              f"\nŚrednia: {suma/ilosc:.2f}")
        break