try:
    nume_fisier = input("Introdu numele fisierului: ").strip()
    if not nume_fisier:
        raise ValueError("Nu ai introdus niciun nume de fisier!")

    with open(nume_fisier, "r") as f:
        continut = f.read()

    numar_cuvinte = len(continut.split())
    print("Numarul total de cuvinte este:")
    print(numar_cuvinte)

except FileNotFoundError:
    print(f"ERROR: Fisierul '{nume_fisier}' nu exista!")
except ValueError as e:
    print(f"ERROR: {e}")
