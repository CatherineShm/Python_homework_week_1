### Zadanie 1.2 | Buty do szewca (ok. 1 godz.)
# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
# (poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
# Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru. Jeśli tak będzie ci wygodniej,
# możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.

dni = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela")

for x, y in enumerate(dni):
    print(y,"-", x, end="|")

oddanie = int(input("\nPodaj numer dnia tygodnia, w którym oddałeś buty do naprawy(wg listy powyżej): "))
dni_naprawy = int(input("Ile dni będzie trwała naprawa: "))
naprawa = int(oddanie + dni_naprawy)

if naprawa >= 7:
    naprawa = naprawa % 7

odbior = dni[naprawa]
print(f"Dzień odbioru butów to: {odbior}.")
