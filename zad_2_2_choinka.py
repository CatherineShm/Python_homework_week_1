# ### Zadanie 2.2 | Choinka
# Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach
# "choinkę" ze znaków `*`. Np. dla parametru 3 powinno się wypisać:
# ```
# *
# * * *
# * * * * *
# ```
# first_name = input("imie: ")
# last_name = input("nazwisok: ")
# b_year = input("rok ur: ")
# profession = input("zawod: ")
# result = f"""
# {"imie i nazwisko:"} {first_name:>10}{last_name.capitalize()}
# {"============================="}
# {"rok urodzenia:"} {b_year:<10}
# {"zawód:"}         {profession}
# """
# print(result)
ilosc = int(input("Podaj liczbę dla swojej choinki: "))
linie = 0
lin = f"{linie:^10}"
print(lin)
while True :
    linie % 2 != 0 and linie <= ilosc
    ligne = "*" * linie
    format = f"{ligne:^10}"
    print(format)
    linie += 1

print("koniec")




