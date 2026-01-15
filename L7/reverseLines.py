try:
    fisier_intrare = input("Introdu numele fisierului de intrare: ").strip()
    fisier_iesire = input("Introdu numele fisierului de iesire: ").strip()

    if not fisier_intrare or not fisier_iesire:
        raise ValueError("Trebuie sa introduci ambele nume de fisier!")

    with open(fisier_intrare, "r", encoding="utf-8") as f_in:
        linii = f_in.readlines()

    with open(fisier_iesire, "w", encoding="utf-8") as f_out:
        for linie in linii:
            f_out.write(linie.strip()[::-1] + "\n")

    print(f"Textul a fost inversat si scris in fisierul '{fisier_iesire}'!")

except FileNotFoundError:
    print(f"ERROR: Fisierul '{fisier_intrare}' nu exista!")
except ValueError as e:
    print(f"ERROR: {e}")