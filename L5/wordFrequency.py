def word_frequency(text):
    text = text.lower()
    for p in ".,!?;:":
        text = text.replace(p, " ")
    dictionar = {}
    for cuvant in text.split():
        dictionar[cuvant] = dictionar.get(cuvant, 0) + 1
    return dictionar

try:
    text_utilizator = input("Introduceti textul: ").strip()
    if not text_utilizator:
        raise ValueError("Nu ati introdus niciun text!")

    rezultat = word_frequency(text_utilizator)
    print("Frecventa cuvintelor este:")
    print(rezultat)

except ValueError as e:
    print(f"ERROR: {e}")