# Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.

lista = [25, 36, 15, -7, 98, 14, 47, -15]
liczba_min = min(lista)
liczba_max = max(lista)

for index, liczba in enumerate(lista):
    (liczba_min[index]), (liczba_max[index]) = (liczba_max[index]), (liczba_min[index])
    print(liczba_min[index])
