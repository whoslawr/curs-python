try:
    text = input("Introdu valorile separate prin virgula: ")
    tupla = tuple(x.strip() for x in text.split(","))

    print(f"Tupla creata este: {tupla}")

    cautat = input("Care e valoarea cautata?: ")

    pozitie = tupla.index(cautat)
    print(f"Valoarea '{cautat}' se gaseste la indexul {pozitie}!")
    
except ValueError:
    print(f"Valoarea '{cautat}' nu exista in tupla!")