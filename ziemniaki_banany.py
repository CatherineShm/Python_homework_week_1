#Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
# ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
# Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
# I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
cena_z = float(input("Podaj cenę ziemniaków (zł/kg): "))
ilosc_z = float(input("Ile kilogramów ziemniaków chciałbyś kupić? "))
naleznosc_z = cena_z * ilosc_z
print("Za", ilosc_z, "kg ziemniaków zapłacisz", round(naleznosc_z, 2), "zł.")
cena_b = float(input("Podaj cenę bananów (zł/kg): "))
ilosc_b = float(input("Ile kilogramów bananów chciałbyś kupić? "))
naleznosc_b = cena_b * ilosc_b
print("Za", ilosc_b, "kg bananów zapłacisz", round(naleznosc_b, 2), "zł.")
naleznosc_r = naleznosc_b + naleznosc_z
print("Za zakupy zapłacisz", round(naleznosc_r, 2), "zł.")
if naleznosc_z < naleznosc_b:
    print("Za banany załpacisz więcej niż za ziemniaki.")
elif naleznosc_b < naleznosc_z:
    print("Za ziemniaki zapłacisz więcej niż za banany.")