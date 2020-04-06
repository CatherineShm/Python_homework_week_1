### Zadanie 1.9 FizzBuzz
# Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
# dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.

for x in range(1, 101):
    
    if x % 3 == 0 and x % 5 == 0:
        print(f"FizzBuzz {x}")
    if x % 5 == 0:
        print(f"Buzz {x}")
    elif x % 3 == 0:
        print(f"Fizz {x}")