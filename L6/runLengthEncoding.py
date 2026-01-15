def run_length_encoding(text):
    if not text:
        return ""
    caracter = text[0]
    contor = 1
    rezultat = ""
    for c in text[1:]:
        if c == caracter:
            contor += 1
        else:
            rezultat += caracter + str(contor)
            caracter = c
            contor = 1
    rezultat += caracter + str(contor)
    return rezultat

try:
    input_text = input("Introdu textul de comprimat (ex: aaabbb): ").strip()
    if not input_text:
        raise ValueError("Nu ai introdus nimic!")

    print("Rezultat:")
    print(run_length_encoding(input_text))

except ValueError as e:
    print(f"ERROR: {e}")