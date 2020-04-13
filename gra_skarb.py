import math
from random import randint


x = 1
y = 1
a = 2
b = 2
skarb = a, b
pozycja_gracza = x, y

ilosc_krokow = 0
odleglosc = abs((x-a)+(y-b))

while True:
    print(f"Pozycja gracza: {pozycja_gracza}")
    ruch = input("Podaj kierunek (użyj klawisz a, d, w lub s): ")
    ilosc_krokow += 1
    if ilosc_krokow > odleglosc * 2: #to nie dziala i nie wiem czemu :(
        a = randint(1, 10)
        b = randint(1, 10)
        ilosc_krokow = 0
        # print(f"nowy skarb {skarb}")
        continue

    odleglosc_przed_krokiem = math.sqrt((a - x) ** 2 + (b - y) ** 2)

    if ruch == "a":
        y -= 1
    elif ruch == "d":
        y += 1
    elif ruch == "w":
        x += 1
    elif ruch == "s":
        x -= 1
    else:
        print("Niepoprawny kierunek.")
        continue

    pozycja_gracza = x, y
    odleglosc_po_kroku = math.sqrt((a - x) ** 2 + (b - y) ** 2)

    while pozycja_gracza == skarb :
        print(f"Pozycja gracza: {pozycja_gracza}")
        print("Wygrałeś!")
        print(f"Żeby znaleść skarb, zrobiłeś {ilosc_krokow} kroków. ")
        exit()

    if x <= 0 or y <= 0:
        print("Wyszedłeś poza pole. Przegrałeś.")
        exit()

    if randint(1, 5) != 5:
        if odleglosc_po_kroku < odleglosc_przed_krokiem:
            print("Ciepło")
        else:
            print("Zimno")