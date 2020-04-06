# Zadanie 2.1 | Zagadka matematyczna
# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka
# jest ich suma(nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
import random


liczba_1 = random.randint(0, 99)
liczba_2 = random.randint(0, 99)
suma = liczba_1 + liczba_2
odpowiedz = int(input(f"Liczby: {liczba_1} i {liczba_2}, podaj sumę: "))

while True:
    if suma == odpowiedz:
        print(f"Dobrze policzyłeś, suma {liczba_1} i {liczba_2} wymonosi {suma}.")
        break
    else:
        odpowiedz = int(input(f"{odpowiedz} nie jest dobrą odpowiedzią. Sprobuj ponownie: "))