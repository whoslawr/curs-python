try:
    valori = input("Introdu numerele separate prin virgula: ")
    numere = [int(x) for x in valori.split(",")]

    if not numere:
        print("Lista este goala!")
    else:
        print(f"Lista ta este: {numere}")
        print(f"Maximul este: {max(numere)}")
        print(f"Minimul este: {min(numere)}")
except ValueError:
    print("ERROR: Asigura-te ca ai introdus doar numere separate prin virgula!")