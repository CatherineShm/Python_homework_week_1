### Zadanie 1.6
#Bilety (ok. 1 godz.)
#Założenia:
#   - 0-6   - wiek przedszkolny - cena biletu: 0
#	- 7-17  - wiek szkolny      - cena biletu: 2.28
#	- 18-64 - wiek dorosły      - cena biletu: 3.80
#	- +65   - wiek emerytalny   - cena biletu: 1.90
#Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić.
#Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić.
# Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli.
print("Cześć! Teraz policzymy razem ile zapłacisz za bilety.")
wiek = int(input("Ile masz lat? "))
ilosc = int(input("Ile biletów chcesz kupić? "))
if wiek >= 0 and wiek <= 6 :
    cena = ilosc * 0
elif wiek >= 7 and wiek <= 17 :
    cena = ilosc * 2.28
elif wiek >= 18 and wiek <= 64 :
    cena = ilosc * 3.80
else :
    cena = ilosc * 1.90

if ilosc == 1 :
    print("Za jeden bilet zapłacisz", round(cena, 1), "złotych.")
elif ilosc == 2 or ilosc == 3 or ilosc == 23 or ilosc == 22 or ilosc == 32 or ilosc == 33 :
    print("Za", ilosc, "bilety zapłacisz", round(cena, 1), "złotych.")
else:
    print("Za", ilosc, "biletów zapłacisz", round(cena, 1), "złotych.")

print("Zapraszamy!")