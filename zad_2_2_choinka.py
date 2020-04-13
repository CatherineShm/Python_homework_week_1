# ### Zadanie 2.2 | Choinka
# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach
# "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
# ```
#     *
#   * * *
# * * * * *
# ```
ilosc = int(input("Podaj liczbę dla swojej choinki: "))
ilosc_znakow = 1
linii = 0
ozdoba = f"{5 * '-':^{ilosc*2}}"
print(ozdoba)

for x in range(0, ilosc):
    for_print = ilosc_znakow * "*"
    print(f"{for_print:^{ilosc*2}}")
    linii += 1
    ilosc_znakow += 2

print(ozdoba)




