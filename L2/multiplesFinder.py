try:
    x = int(input("Introdu numarul x (baza): "))
    y = int(input("Introdu numarul y (limita): "))

    if x <= 0 or y <= 0:
        print("ERROR: Introdu doar numere naturale pozitive!")
    else:
        start, stop = min(x, y), max(x, y)

        if start == 0:
            print("ERROR: 0 nu e un numar valid!")
        else:
            multipli = list(range(start, stop, start))
            print(f"Multiplii lui {start} mai mici decat {stop} sunt:")
            for m in multipli:
                print(m)

except ValueError:
    print("ERROR: Introdu doar numere naturale pozitive!")