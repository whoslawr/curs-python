try:
    text = input("Introdu numerele separate prin virgula: ")
    numere = [int(x.strip()) for x in text.split(",")]

    rezultat = []
    for n in numere:
        if n not in rezultat:
            rezultat.append(n)

    print(f"Lista originala: {numere}")
    print(f"Lista fara duplicate: {rezultat}")
except ValueError:
    print("ERROR: Introdu doar numere intregi, separate prin virgula!")