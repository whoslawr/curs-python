def palindrom(text):
    text = text.lower()
    return text == text[::-1]

try:
    cuvant = input("Introdu un cuvant: ")
    if not cuvant.isalpha():
        raise ValueError
    if palindrom(cuvant):
        print("Este palindrom.")
    else:
        print("Nu este palindrom.")
except ValueError:
    print("Introdu doar litere.")