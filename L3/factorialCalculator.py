def factorial(n):
    rezultat = 1
    for i in range(1, n + 1):
        rezultat *= i
    return rezultat

try:
    n = int(input("Introdu un numar intreg: "))
    if n < 0:
        print("ERROR: Trebuie sa introduci un numar natural!")
    else:
        print(f"Factorialul lui {n} este: {factorial(n)}")
except ValueError:
    print("ERROR: Trebuie sa introduci un numar natural!")