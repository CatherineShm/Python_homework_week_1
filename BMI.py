### Zadanie 1.3 | Współczynnik BMI (ok. 2 godz.)
#Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
#oraz podsumowanie informujące o stanie/zaleceniach.
import time
print("Cześć, ten program obliczy twój BMI(Body Mass Index). Zaczynamy? ")
time.sleep(1)
masa = float(input("Jaka jest twoja waga (w kg) ? "))
wzrost = float(input("Podaj swój wzrost w cm: ")) / 100
bmi = masa / (wzrost * wzrost)
if bmi < 18.5 :
    classif = "niedowaga"
elif bmi >= 18.5 and bmi <= 24.9 :
    classif = "waga prawidłowa"
elif bmi >= 25 and bmi <= 29.9 :
    classif = "nadwaga"
else:
    classif = "otyłość"
print("Twoje BMI wynosi", round(bmi, 2), ".")
print("-------------")
print("Klasyfikacja twojego BMI: ", classif, ".")
print("-------------")
time.sleep(1)
print("Życzymy zdrowia!")