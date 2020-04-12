# ### Zadanie 2.4 | Zgadnij liczbę z zakresu
# Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
# Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
# Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie
# udało się zgadnąć liczbę.

import random


liczba = random.randint(0, 1000)
ilosc_prob = 0

while True:
    odpowiedz = input("Zgadnij liczbę z zakresu od 0 do 999 : ")
    ilosc_prob += 1

    if int(odpowiedz) < int(liczba):
        print("Podałeś za małą liczbę.")

    if int(odpowiedz) > int(liczba):
        print("Podałeś za dużą liczbę.")

    if int(odpowiedz) == int(liczba):
        print(f"Gratulacje, zgadłeś liczbę z {ilosc_prob} sproby! \nLiczba to {liczba}.")
        break