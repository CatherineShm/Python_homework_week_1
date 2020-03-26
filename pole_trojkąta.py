### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
#Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
#(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
#Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
#Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
#``` // import math // x = math.sqrt(10) // ```
import math
import time
print("Ten program pomoże obliczyć Ci pole trójkąta. ")
print("Przy wprowadzaniu danych, pamiętaj, że suma każdych dwóch stron powinna być większa niż trzecia strona.")
time.sleep(2)
a = int(input("Podaj długość pierwszej strony (w cm): "))
b = int(input("Podaj długość drugiej strony (w cm): "))
c = int(input("Podaj długość trzeciej strony (w cm): "))
if a + b <= c or a + c <= b or b + c <= a :
    print("Trójkąt o takich stronach nie istnieje.")
else:
    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("Pole trójkąta o stronach", a, ",", b, "i", c, "cm jest", round(pole, 2), "cm.")