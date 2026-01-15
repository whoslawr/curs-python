def inverted_index(documents):
    index_dict = {}
    for i, text in enumerate(documents):
        for cuvant in text.split():
            index_dict.setdefault(cuvant, set()).add(i)
    return index_dict

try:
    numar = int(input("Cate propozitii vrei sa introduci?: "))
    if numar <= 0:
        raise ValueError("Numar invalid!")

    lista_documente = []
    for k in range(numar):
        propozitie = input(f"Documentul {k}: ")
        lista_documente.append(propozitie)

    rezultat = inverted_index(lista_documente)

    print("\n--- Afisare detaliata ---")
    for cuvant, doc_set in rezultat.items():
        print(f"{cuvant}: {doc_set}")

except ValueError:
    print("ERROR: Trebuie sa introduci un numar valid de propozitii!")