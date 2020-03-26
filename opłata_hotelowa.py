#Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza, ile trzeba zapłacić. Zasady są takie:
#- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
#- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
#	- 200 zł za noc, jeśli nocują jedną noc
#	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
#	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
#- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
#Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
# czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
print("Serdecznie zapraszamy do \"Naszego\" hotelu")
nocy = int(input("Ile nocy będzie trwać twój pobyt? "))
wiek = int(input("Ile masz lat? "))
if wiek < 18 :
    cena_1 = nocy * 100
    print("Za", nocy, "noc(y) pobytu zapłacisz", cena_1, "złotych.")
elif wiek >= 18 and wiek < 65 :
    if int(nocy) == 1 :
        cena_2 = 200
        print("Za jedną noc zapłacisz", cena_2, "złotych.")
    elif nocy <= 2 or nocy < 5 :
       cena_3 = nocy * 180
       print("Za", nocy, "zapłacisz", cena_3, "złotych.")
    else :
        cena_4 = nocy * 150
        print("Za", nocy, "nocy zapłacisz", cena_4, "złotych.")
else:
    if int(nocy) == 1 :
       cena_5 = 200 - (200 * 0.1)
       print("Za jedną noc zapłacisz", cena_5, "złotych.")
    elif nocy <= 2 or nocy < 5 :
         cena_6 = int(nocy) * (180 - 180 * 0.1)
         print("Za", nocy, "nocy zapłacisz", cena_6, "złotych.")
    else :
        cena_7 = int(nocy) * (150 - 150 * 0.1)
        print("Za", nocy, "nocy zapłacisz", cena_7, "złotych.")

print("Życzymy miłego pobytu!")