try:
    fisier_intrare = input("Introdu numele fisierului de intrare: ").strip()
    fisier_iesire = input("Introdu numele fisierului de iesire: ").strip()
    cuvant_cheie = input("Introdu cuvantul cheie: ").strip()

    if not fisier_intrare or not fisier_iesire or not cuvant_cheie:
        raise ValueError("Toate campurile trebuie completate!")

    with open(fisier_intrare, "r", encoding="utf-8") as f_in:
        linii = f_in.readlines()

    with open(fisier_iesire, "w", encoding="utf-8") as f_out:
        for linie in linii:
            if cuvant_cheie in linie:
                f_out.write(linie)

    print(f"Liniile care contin '{cuvant_cheie}' au fost salvate in '{fisier_iesire}'!")

except FileNotFoundError:
    print(f"ERROR: Fisierul '{fisier_intrare}' nu exista!")
except ValueError as e:
    print(f"ERROR: {e}")