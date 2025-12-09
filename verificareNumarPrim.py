numar = int(input("Introdu un numar intreg: "))

if numar <= 1:
    print("Numarul nu este prim!")
else:
    isPrime = True

    for divizor in range(2, numar):
        if numar % divizor == 0:
            isPrime = False
            break

    if isPrime:
        print("Numarul este prim.")
    else:
        print("Numarul NU este prim.")