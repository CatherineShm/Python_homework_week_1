# Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.

lista = [25, 36, 15, -7, 98, 14, 47, -15]
print(lista)

liczba_min = min(lista)
liczba_max = max(lista)

index_max = lista.index(liczba_max)
index_min = lista.index(liczba_min)

lista[index_min], lista[index_max] = lista[index_max], lista[index_min]
print(lista)