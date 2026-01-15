def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

try:
    input_text = input("Introdu propozitia: ").strip()
    if not input_text:
        raise ValueError("Nu ai introdus nimic!")

    print("Propozitia inversata:")
    print(reverse_words(input_text))

except ValueError as e:
    print(f"ERROR: {e}")