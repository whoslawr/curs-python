try:
    n = int(input("Introdu numarul n: "))
    if n <= 0:
        print("ERROR: Te rog introdu un numar mai mare decat 0.")
    else:
        print(f"Numerele impare pana la {n} sunt:")
        for valoare in range(1, n + 1, 2):
            print(valoare)
except ValueError:
    print("ERROR: Te rog introdu un numar natural valid (fara litere).")